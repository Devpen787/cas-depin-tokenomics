#!/usr/bin/env python3
"""Validate and query the thesis agent knowledge-skill graph."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple


GRAPH_PATH = Path(__file__).resolve().parents[1] / '.agent' / 'knowledge-skill-graph.json'
ALLOWED_NODE_TYPES = {'knowledge', 'skill', 'task', 'risk', 'artefact'}
ALLOWED_EDGE_TYPES = {'REQUIRES', 'ROUTES_TO', 'MITIGATES', 'UPDATES', 'PREREQUISITE'}
PIN_PATTERN = re.compile(r'^git:[0-9a-fA-F]{7,40}$')
REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Node:
    id: str
    type: str
    name: str
    description: str
    tags: Tuple[str, ...]
    file: str | None = None


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    type: str
    rationale: str | None = None


@dataclass(frozen=True)
class Graph:
    nodes: Dict[str, Node]
    edges: Tuple[Edge, ...]

    def edges_by_type(self, edge_type: str) -> List[Edge]:
        return [edge for edge in self.edges if edge.type == edge_type]

    def node_ids_by_type(self, node_type: str) -> List[str]:
        return sorted(node_id for node_id, node in self.nodes.items() if node.type == node_type)


def load_graph(path: Path) -> Graph:
    raw = json.loads(path.read_text(encoding='utf-8'))
    nodes: Dict[str, Node] = {}

    for item in raw.get('nodes', []):
        node = Node(
            id=item['id'],
            type=item['type'],
            name=item.get('name', item['id']),
            description=item.get('description', ''),
            tags=tuple(item.get('tags', [])),
            file=item.get('file'),
        )
        nodes[node.id] = node

    edges = tuple(
        Edge(
            source=item['source'],
            target=item['target'],
            type=item['type'],
            rationale=item.get('rationale'),
        )
        for item in raw.get('edges', [])
    )
    return Graph(nodes=nodes, edges=edges)


def run_git(args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ['git', *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def get_head_sha() -> str | None:
    result = run_git(['rev-parse', '--verify', 'HEAD'])
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def get_dirty_state() -> bool | None:
    result = run_git(['status', '--porcelain'])
    if result.returncode != 0:
        return None
    return bool(result.stdout.strip())


def has_node_level_source_pin(raw_graph: Dict[str, object]) -> bool:
    raw_nodes = raw_graph.get('nodes')
    if not isinstance(raw_nodes, list):
        return False
    for raw_node in raw_nodes:
        if not isinstance(raw_node, dict):
            continue
        if raw_node.get('type') != 'knowledge':
            continue
        source_version = raw_node.get('source_version')
        if isinstance(source_version, str) and source_version.strip():
            return True
    return False


def validate_policy(raw_graph: Dict[str, object], enforce_dirty: bool) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    graph_pin = raw_graph.get('graph_source_version')
    graph_pin_value = graph_pin if isinstance(graph_pin, str) and graph_pin.strip() else None
    node_pin_present = has_node_level_source_pin(raw_graph)

    if graph_pin_value and not PIN_PATTERN.fullmatch(graph_pin_value):
        errors.append('graph_source_version must match ^git:[0-9a-fA-F]{7,40}$.')

    if not graph_pin_value and not node_pin_present:
        errors.append('Missing source version pin: provide graph_source_version or knowledge node source_version.')

    head_sha = get_head_sha()
    if graph_pin_value and head_sha and graph_pin_value.startswith('git:'):
        pinned_sha = graph_pin_value.split(':', 1)[1]
        if not head_sha.startswith(pinned_sha):
            warnings.append(
                f'WARNING: graph_source_version does not match current HEAD (pinned={pinned_sha}, head={head_sha}).',
            )

    dirty_state = get_dirty_state()
    if dirty_state is None:
        warnings.append('WARNING: unable to determine git working tree status.')
    elif dirty_state and enforce_dirty:
        errors.append('Refusing run: git working tree is dirty.')
    elif dirty_state:
        warnings.append('WARNING: git working tree is dirty; continuing because this command is read-only.')

    return errors, warnings


def validate_graph(graph: Graph) -> List[str]:
    errors: List[str] = []

    for node_id, node in graph.nodes.items():
        if node.type not in ALLOWED_NODE_TYPES:
            errors.append(f'Invalid node type for {node_id}: {node.type}')

    seen_edges: Set[Tuple[str, str, str]] = set()
    for edge in graph.edges:
        if edge.type not in ALLOWED_EDGE_TYPES:
            errors.append(f'Invalid edge type {edge.type} ({edge.source} -> {edge.target})')
        if edge.source not in graph.nodes:
            errors.append(f'Unknown edge source: {edge.source}')
        if edge.target not in graph.nodes:
            errors.append(f'Unknown edge target: {edge.target}')
        signature = (edge.source, edge.target, edge.type)
        if signature in seen_edges:
            errors.append(f'Duplicate edge: {signature}')
        seen_edges.add(signature)

    errors.extend(validate_prerequisite_graph(graph))
    return errors


def validate_prerequisite_graph(graph: Graph) -> List[str]:
    errors: List[str] = []
    prereq_edges = [edge for edge in graph.edges if edge.type == 'PREREQUISITE']
    adjacency: Dict[str, List[str]] = defaultdict(list)
    in_degree: Dict[str, int] = defaultdict(int)
    skill_nodes = set(graph.node_ids_by_type('skill'))

    for edge in prereq_edges:
        if edge.source not in skill_nodes or edge.target not in skill_nodes:
            errors.append(
                f'PREREQUISITE edges must connect skills only: {edge.source} -> {edge.target}',
            )
            continue
        # Direction: source depends on target. For cycle detection we invert.
        adjacency[edge.target].append(edge.source)
        in_degree[edge.source] += 1
        if edge.target not in in_degree:
            in_degree[edge.target] = in_degree[edge.target]

    queue: deque[str] = deque(node for node, degree in in_degree.items() if degree == 0)
    visited = 0

    while queue:
        current = queue.popleft()
        visited += 1
        for neighbour in adjacency[current]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if in_degree and visited != len(in_degree):
        errors.append('PREREQUISITE skill graph contains a cycle.')
    return errors


def collect_task_skills(graph: Graph, task_id: str) -> List[str]:
    if task_id not in graph.nodes:
        raise ValueError(f'Unknown task id: {task_id}')
    if graph.nodes[task_id].type != 'task':
        raise ValueError(f'Node is not a task: {task_id}')

    direct_skills = [
        edge.target
        for edge in graph.edges
        if edge.type == 'ROUTES_TO' and edge.source == task_id and graph.nodes.get(edge.target, None)
    ]
    skill_set: Set[str] = set(direct_skills)

    # Expand prerequisites transitively.
    prereq_by_skill: Dict[str, List[str]] = defaultdict(list)
    for edge in graph.edges:
        if edge.type == 'PREREQUISITE':
            prereq_by_skill[edge.source].append(edge.target)

    stack: List[str] = list(direct_skills)
    while stack:
        skill_id = stack.pop()
        for prereq_id in prereq_by_skill.get(skill_id, []):
            if prereq_id not in skill_set:
                skill_set.add(prereq_id)
                stack.append(prereq_id)

    return topological_skill_order(graph, skill_set)


def topological_skill_order(graph: Graph, skill_ids: Iterable[str]) -> List[str]:
    selected = set(skill_ids)
    adjacency: Dict[str, List[str]] = defaultdict(list)
    in_degree: Dict[str, int] = {skill_id: 0 for skill_id in selected}

    for edge in graph.edges:
        if edge.type != 'PREREQUISITE':
            continue
        dependent, prerequisite = edge.source, edge.target
        if dependent in selected and prerequisite in selected:
            adjacency[prerequisite].append(dependent)
            in_degree[dependent] += 1

    queue: deque[str] = deque(sorted(node for node, degree in in_degree.items() if degree == 0))
    ordered: List[str] = []

    while queue:
        current = queue.popleft()
        ordered.append(current)
        for neighbour in sorted(adjacency[current]):
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(ordered) != len(selected):
        unresolved = sorted(selected.difference(ordered))
        raise ValueError(f'Cannot resolve skill order because of a cycle: {", ".join(unresolved)}')

    return ordered


def skill_manifest(graph: Graph, skill_id: str) -> Dict[str, List[str]]:
    if skill_id not in graph.nodes:
        raise ValueError(f'Unknown skill id: {skill_id}')
    if graph.nodes[skill_id].type != 'skill':
        raise ValueError(f'Node is not a skill: {skill_id}')

    requires = sorted(
        edge.target
        for edge in graph.edges
        if edge.type == 'REQUIRES' and edge.source == skill_id
    )
    mitigates = sorted(
        edge.target
        for edge in graph.edges
        if edge.type == 'MITIGATES' and edge.source == skill_id
    )
    updates = sorted(
        edge.target
        for edge in graph.edges
        if edge.type == 'UPDATES' and edge.source == skill_id
    )
    prerequisites = sorted(
        edge.target
        for edge in graph.edges
        if edge.type == 'PREREQUISITE' and edge.source == skill_id
    )
    return {
        'requires': requires,
        'mitigates': mitigates,
        'updates': updates,
        'prerequisites': prerequisites,
    }


def render_node_list(graph: Graph, node_ids: Iterable[str]) -> str:
    lines: List[str] = []
    for node_id in node_ids:
        node = graph.nodes[node_id]
        lines.append(f'- {node.id}: {node.name}')
    return '\n'.join(lines)


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description='Validate and query the thesis knowledge-skill graph.',
    )
    parser.add_argument(
        '--graph',
        type=Path,
        default=GRAPH_PATH,
        help=f'Path to graph JSON (default: {GRAPH_PATH})',
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate schema links and prerequisite DAG constraints.',
    )
    parser.add_argument(
        '--validate-policy',
        action='store_true',
        help='Validate source pin and execution-gating policy.',
    )
    parser.add_argument(
        '--list-tasks',
        action='store_true',
        help='List available task nodes.',
    )
    parser.add_argument(
        '--list-skills',
        action='store_true',
        help='List available skill nodes.',
    )
    parser.add_argument(
        '--task',
        type=str,
        help='Show routed skills (including prerequisites) for a task id.',
    )
    parser.add_argument(
        '--skill',
        type=str,
        help='Show requirements, risks mitigated, and artefacts updated for a skill id.',
    )
    args = parser.parse_args(argv)

    raw_graph = json.loads(args.graph.read_text(encoding='utf-8'))
    graph = load_graph(args.graph)
    pin_value = raw_graph.get('graph_source_version')
    pin_banner = pin_value if isinstance(pin_value, str) and pin_value.strip() else '(none)'
    print(f'Graph source pin: {pin_banner}')

    if not any([args.validate, args.validate_policy, args.list_tasks, args.list_skills, args.task, args.skill]):
        parser.print_help()
        return 0

    if args.validate:
        errors = validate_graph(graph)
        if errors:
            print('Validation failed:')
            for error in errors:
                print(f'  - {error}')
            return 1
        print('Validation passed: graph structure is consistent.')

    is_listing_command = bool(args.list_tasks or args.list_skills)
    is_execution_command = bool(args.task or args.skill)

    if args.validate_policy:
        policy_errors, policy_warnings = validate_policy(raw_graph, enforce_dirty=True)
        for warning in policy_warnings:
            print(warning)
        if policy_errors:
            print('Policy validation failed:')
            for error in policy_errors:
                print(f'  - {error}')
            return 1
        print('Policy validation passed.')

    if is_execution_command:
        policy_errors, policy_warnings = validate_policy(raw_graph, enforce_dirty=True)
        for warning in policy_warnings:
            print(warning)
        if policy_errors:
            print('Policy validation failed:')
            for error in policy_errors:
                print(f'  - {error}')
            return 1
    elif is_listing_command and not args.validate_policy:
        # Listing commands are read-only: warn but do not refuse.
        policy_errors, policy_warnings = validate_policy(raw_graph, enforce_dirty=False)
        for warning in policy_warnings:
            print(warning)
        for error in policy_errors:
            print(f'WARNING: {error}')

    if args.list_tasks:
        print(render_node_list(graph, graph.node_ids_by_type('task')))

    if args.list_skills:
        print(render_node_list(graph, graph.node_ids_by_type('skill')))

    if args.task:
        routed_skills = collect_task_skills(graph, args.task)
        print(f'Task: {args.task}')
        for idx, skill_id in enumerate(routed_skills, start=1):
            print(f'  {idx}. {skill_id} - {graph.nodes[skill_id].name}')

    if args.skill:
        manifest = skill_manifest(graph, args.skill)
        print(f'Skill: {args.skill} ({graph.nodes[args.skill].name})')
        for key in ['prerequisites', 'requires', 'mitigates', 'updates']:
            print(f'  {key}:')
            values = manifest[key]
            if not values:
                print('    - (none)')
                continue
            for value in values:
                label = graph.nodes[value].name if value in graph.nodes else value
                print(f'    - {value} ({label})')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
