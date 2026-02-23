#!/usr/bin/env python3
"""Validate and query the thesis agent knowledge-skill graph."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple


GRAPH_PATH = Path(__file__).resolve().parents[1] / '.agent' / 'knowledge-skill-graph.json'
ALLOWED_NODE_TYPES = {'knowledge', 'skill', 'task', 'risk', 'artefact'}
ALLOWED_EDGE_TYPES = {'REQUIRES', 'ROUTES_TO', 'MITIGATES', 'UPDATES', 'PREREQUISITE'}
PIN_PATTERN = re.compile(r'^git:[0-9a-fA-F]{7,40}$')
REPO_ROOT = Path(__file__).resolve().parents[1]
SECTION_ORDER = ['SUMMARY', 'TRACEABILITY', 'RESULT', 'GAPS']
SECTION_HEADING_PATTERN = re.compile(r'^##\s*(SUMMARY|TRACEABILITY|RESULT|GAPS)\s*$')
BULLET_START_PATTERN = re.compile(r'^\s*(?:[-*]|\d+\.)\s+')
CLAIM_ID_PATTERN = re.compile(r'\[CLAIM_ID:([A-Za-z0-9._:-]+)\]')
NONASSERTIVE_PATTERN = re.compile(r'\[NONASSERTIVE\]')
NEW_CLAIM_PATTERN = re.compile(r'NEW_CLAIM\{([^}]*)\}')
PROVENANCE_PATTERN = re.compile(r'^\s*PROVENANCE\|')


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


def run_git(args: List[str]) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            ['git', *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None


def get_head_sha() -> str | None:
    result = run_git(['rev-parse', '--verify', 'HEAD'])
    if result is None:
        return None
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def get_dirty_state() -> bool | None:
    result = run_git(['status', '--porcelain'])
    if result is None:
        return None
    if result.returncode != 0:
        return None
    return bool(result.stdout.strip())


def is_ancestor(ancestor_sha: str, head_sha: str) -> bool | None:
    result = run_git(['merge-base', '--is-ancestor', ancestor_sha, head_sha])
    if result is None:
        return None
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    return None


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


def get_task_preferred_order(raw_graph: Dict[str, object], task_id: str) -> List[str]:
    raw_nodes = raw_graph.get('nodes')
    if not isinstance(raw_nodes, list):
        return []

    for raw_node in raw_nodes:
        if not isinstance(raw_node, dict):
            continue
        if raw_node.get('id') != task_id:
            continue
        preferred_order = raw_node.get('preferred_order')
        if not isinstance(preferred_order, list):
            return []
        return [item for item in preferred_order if isinstance(item, str)]

    return []


def order_skills_with_preference(
    graph: Graph,
    skill_ids: Iterable[str],
    preferred_order: List[str],
) -> List[str]:
    selected = set(skill_ids)
    if not selected:
        return []

    if not preferred_order:
        return topological_skill_order(graph, selected)

    rank_by_id: Dict[str, int] = {}
    for idx, skill_id in enumerate(preferred_order):
        if skill_id in selected and skill_id not in rank_by_id:
            rank_by_id[skill_id] = idx

    adjacency: Dict[str, List[str]] = defaultdict(list)
    in_degree: Dict[str, int] = {skill_id: 0 for skill_id in selected}

    for edge in graph.edges:
        if edge.type != 'PREREQUISITE':
            continue
        dependent, prerequisite = edge.source, edge.target
        if dependent in selected and prerequisite in selected:
            adjacency[prerequisite].append(dependent)
            in_degree[dependent] += 1

    available: Set[str] = {skill_id for skill_id, degree in in_degree.items() if degree == 0}
    ordered: List[str] = []

    while available:
        current = min(
            available,
            key=lambda skill_id: (rank_by_id.get(skill_id, float('inf')), skill_id),
        )
        available.remove(current)
        ordered.append(current)
        for neighbour in adjacency[current]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                available.add(neighbour)

    if len(ordered) != len(selected):
        unresolved = sorted(selected.difference(ordered))
        raise ValueError(f'Cannot resolve skill order because of a cycle: {", ".join(unresolved)}')

    return ordered


def validate_preferred_order_metadata(raw_graph: Dict[str, object], graph: Graph) -> List[str]:
    warnings: List[str] = []
    raw_nodes = raw_graph.get('nodes')
    if not isinstance(raw_nodes, list):
        return warnings

    skill_ids = set(graph.node_ids_by_type('skill'))
    for raw_node in raw_nodes:
        if not isinstance(raw_node, dict):
            continue
        if raw_node.get('type') != 'task':
            continue
        task_id = raw_node.get('id')
        if not isinstance(task_id, str):
            continue

        preferred_order = raw_node.get('preferred_order')
        if not isinstance(preferred_order, list):
            continue

        preferred_skills = [item for item in preferred_order if isinstance(item, str)]
        if len(preferred_skills) != len(set(preferred_skills)):
            warnings.append(f'WARNING: task {task_id} preferred_order contains duplicate skill ids.')

        try:
            routed_closure = set(collect_task_skills(graph, task_id))
        except ValueError:
            continue

        for skill_id in preferred_skills:
            if skill_id not in skill_ids:
                warnings.append(
                    f'WARNING: task {task_id} preferred_order references non-skill id: {skill_id}.',
                )
            elif skill_id not in routed_closure:
                warnings.append(
                    f'WARNING: task {task_id} preferred_order references skill outside routed closure: {skill_id}.',
                )

    return warnings


def validate_policy(
    raw_graph: Dict[str, object],
    graph: Graph,
    enforce_dirty: bool,
    allow_dirty_override: bool = False,
) -> Tuple[List[str], List[str]]:
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
    if head_sha is None:
        warnings.append('WARNING: unable to determine git HEAD (git unavailable?).')
    if graph_pin_value and head_sha and graph_pin_value.startswith('git:'):
        pinned_sha = graph_pin_value.split(':', 1)[1]
        anc = is_ancestor(pinned_sha, head_sha)
        if anc is False:
            warnings.append(
                f'WARNING: graph_source_version does not match current HEAD (pinned={pinned_sha}, head={head_sha}).',
            )
        elif anc is None:
            warnings.append('WARNING: unable to determine git ancestry for graph_source_version vs HEAD.')

    dirty_state = get_dirty_state()
    if dirty_state is None:
        warnings.append('WARNING: unable to determine git working tree status.')
        if enforce_dirty:
            errors.append('Refusing run: cannot determine git working tree status (git unavailable).')
    elif dirty_state and enforce_dirty:
        errors.append('Refusing run: git working tree is dirty.')
    elif dirty_state and allow_dirty_override:
        warnings.append('WARNING: git working tree is dirty; proceeding due to --allow-dirty.')
    elif dirty_state:
        warnings.append('WARNING: git working tree is dirty; continuing because this command is read-only.')

    warnings.extend(validate_preferred_order_metadata(raw_graph, graph))
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


def discover_ledgers() -> List[Path]:
    references_dir = REPO_ROOT / 'references'
    canonical = references_dir / 'claim_ledger_master.csv'
    globbed = sorted(references_dir.glob('**/claim_ledger*.csv'))
    ordered: List[Path] = []
    if canonical.exists():
        ordered.append(canonical)
    for path in globbed:
        if path not in ordered:
            ordered.append(path)
    if not ordered:
        raise ValueError('No claim ledgers found (expected references/**/claim_ledger*.csv).')
    return ordered


def load_claim_ids(ledger_paths: List[Path]) -> Set[str]:
    claim_ids: Set[str] = set()
    for ledger_path in ledger_paths:
        with ledger_path.open('r', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            if not reader.fieldnames or 'claim_id' not in reader.fieldnames:
                raise ValueError(f'Ledger missing claim_id column: {ledger_path}')
            for row in reader:
                claim_id = (row.get('claim_id') or '').strip()
                if claim_id:
                    claim_ids.add(claim_id)
    if not claim_ids:
        raise ValueError('No claim IDs found in discovered ledgers.')
    return claim_ids


def parse_sections(text: str) -> Tuple[List[str], Dict[str, Tuple[int, int, int]]]:
    lines = text.splitlines(keepends=True)
    headings: List[Tuple[str, int]] = []
    seen: Dict[str, int] = {}
    for index, line in enumerate(lines):
        match = SECTION_HEADING_PATTERN.fullmatch(line.rstrip('\r\n'))
        if match:
            name = match.group(1)
            if name in seen:
                raise ValueError(
                    f'Duplicate required heading "{name}" at line {index + 1} '
                    f'(first seen at line {seen[name] + 1}).',
                )
            seen[name] = index
            headings.append((name, index))

    names = [name for name, _ in headings]
    missing = [name for name in SECTION_ORDER if name not in seen]
    if missing:
        raise ValueError('Missing required heading(s): ' + ', '.join(missing) + '.')
    if names != SECTION_ORDER:
        raise ValueError(
            'Required headings are out of order. Expected: '
            + ' / '.join(SECTION_ORDER)
            + '; found: '
            + ' / '.join(names)
            + '.'
        )

    sections: Dict[str, Tuple[int, int, int]] = {}
    for idx, (name, heading_index) in enumerate(headings):
        body_start = heading_index + 1
        body_end = headings[idx + 1][1] if idx + 1 < len(headings) else len(lines)
        sections[name] = (heading_index, body_start, body_end)
    return lines, sections


def split_result_units(result_text: str) -> List[Tuple[str, str]]:
    units: List[Tuple[str, str]] = []
    current_lines: List[str] = []
    current_type: str | None = None

    def flush() -> None:
        nonlocal current_lines, current_type
        if not current_lines or current_type is None:
            current_lines = []
            current_type = None
            return
        units.append((current_type, '\n'.join(current_lines).strip()))
        current_lines = []
        current_type = None

    for line in result_text.splitlines():
        if not line.strip():
            flush()
            continue

        if BULLET_START_PATTERN.match(line):
            flush()
            current_type = 'bullet'
            current_lines = [line]
            continue

        if current_type == 'bullet':
            if line.startswith('\t'):
                current_lines.append(line)
                continue
            stripped = line.lstrip(' ')
            indent = len(line) - len(stripped)
            if 0 < indent <= 2 and not BULLET_START_PATTERN.match(stripped):
                current_lines.append(line)
                continue

        if current_type != 'paragraph':
            flush()
            current_type = 'paragraph'
            current_lines = [line]
        else:
            current_lines.append(line)

    flush()
    return units


def validate_new_claims(unit_text: str) -> List[str]:
    errors: List[str] = []
    for match in NEW_CLAIM_PATTERN.finditer(unit_text):
        body = match.group(1)
        parsed: Dict[str, str] = {}
        for part in body.split(';'):
            token = part.strip()
            if not token or '=' not in token:
                continue
            key, value = token.split('=', 1)
            normalized_key = key.strip()
            if normalized_key in {'id', 'statement', 'evidence_needed'} and value.strip():
                parsed[normalized_key] = value.strip()
        missing_keys = [key for key in ['id', 'statement', 'evidence_needed'] if key not in parsed]
        if missing_keys:
            errors.append(
                'NEW_CLAIM block missing required keys: '
                + ', '.join(missing_keys)
                + f' ({match.group(0)})'
            )
    return errors


def validate_result_units(units: List[Tuple[str, str]], known_claim_ids: Set[str]) -> List[str]:
    errors: List[str] = []
    for index, (unit_type, unit_text) in enumerate(units, start=1):
        unit_label = f'{unit_type} #{index}'
        for error in validate_new_claims(unit_text):
            errors.append(f'{unit_label}: {error}')

        claim_ids = CLAIM_ID_PATTERN.findall(unit_text)
        has_nonassertive = bool(NONASSERTIVE_PATTERN.search(unit_text))
        has_new_claim = bool(NEW_CLAIM_PATTERN.search(unit_text))

        if not claim_ids and not has_nonassertive and not has_new_claim:
            errors.append(f'{unit_label}: missing [CLAIM_ID:<id>] or [NONASSERTIVE].')

        for claim_id in claim_ids:
            if claim_id not in known_claim_ids:
                errors.append(f'{unit_label}: unknown CLAIM_ID "{claim_id}".')
    return errors


def build_provenance(
    model_id: str,
    task_id: str,
    graph_pin: str,
    graph_hash: str,
    timestamp_utc: str,
    affected_files: str,
) -> str:
    return (
        f'PROVENANCE|model={model_id}|task={task_id}|graph_pin={graph_pin}|graph_hash={graph_hash}'
        f'|timestamp_utc={timestamp_utc}|affected_files={affected_files}'
    )


def stamp_traceability(
    lines: List[str],
    sections: Dict[str, Tuple[int, int, int]],
    provenance_line: str,
) -> Tuple[str, bool]:
    _, trace_start, trace_end = sections['TRACEABILITY']
    newline = '\n'
    for line in lines:
        if line.endswith('\r\n'):
            newline = '\r\n'
            break
        if line.endswith('\n'):
            newline = '\n'
            break
    provenance_with_newline = provenance_line + newline

    provenance_indices = [
        idx
        for idx in range(trace_start, trace_end)
        if PROVENANCE_PATTERN.match(lines[idx].rstrip('\r\n'))
    ]

    if provenance_indices:
        first_index = provenance_indices[0]
        if len(provenance_indices) == 1 and lines[first_index] == provenance_with_newline:
            return ''.join(lines), False
        lines[first_index] = provenance_with_newline
        for extra_index in reversed(provenance_indices[1:]):
            del lines[extra_index]
        return ''.join(lines), True

    lines.insert(trace_end, provenance_with_newline)
    return ''.join(lines), True


def validate_output_file(
    output_path: Path,
    task_id: str,
    model_id: str | None,
    affected_files: str | None,
    raw_graph: Dict[str, object],
    stamp: bool,
) -> List[str]:
    errors: List[str] = []
    if not output_path.exists():
        return [f'Output file not found: {output_path}']

    with output_path.open('r', encoding='utf-8', newline='') as handle:
        text = handle.read()
    try:
        lines, sections = parse_sections(text)
    except ValueError as error:
        return [str(error)]

    try:
        ledgers = discover_ledgers()
        known_claim_ids = load_claim_ids(ledgers)
    except ValueError as error:
        return [str(error)]

    _, result_start, result_end = sections['RESULT']
    result_text = ''.join(lines[result_start:result_end])
    result_units = split_result_units(result_text)
    if not result_units:
        errors.append('RESULT section is empty.')
    else:
        errors.extend(validate_result_units(result_units, known_claim_ids))

    if not stamp:
        return errors

    if not model_id:
        errors.append('Missing required --model-id for provenance stamp.')
    if not task_id:
        errors.append('Missing task/skill identifier for provenance stamp.')
    if not affected_files:
        errors.append('Missing required --affected-files for provenance stamp.')
    if errors:
        return errors

    graph_pin_raw = raw_graph.get('graph_source_version')
    graph_pin = graph_pin_raw if isinstance(graph_pin_raw, str) and graph_pin_raw.strip() else '(none)'
    graph_hash = hashlib.sha256(GRAPH_PATH.read_bytes()).hexdigest()
    timestamp_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    provenance_line = build_provenance(
        model_id=model_id,
        task_id=task_id,
        graph_pin=graph_pin,
        graph_hash=graph_hash,
        timestamp_utc=timestamp_utc,
        affected_files=affected_files,
    )
    stamped_text, changed = stamp_traceability(lines, sections, provenance_line)
    if changed:
        output_path.write_text(stamped_text, encoding='utf-8')

    return errors


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
    parser.add_argument(
        '--allow-dirty',
        action='store_true',
        help='Allow execution-capable commands to proceed on dirty git tree.',
    )
    parser.add_argument(
        '--validate-output',
        type=Path,
        help='Validate a structured output markdown file using claim gate + output contract.',
    )
    parser.add_argument(
        '--model-id',
        type=str,
        help='Model identifier used in provenance stamp.',
    )
    parser.add_argument(
        '--affected-files',
        type=str,
        help='Comma-separated affected file paths for provenance stamp.',
    )
    parser.add_argument(
        '--no-stamp',
        action='store_true',
        help='Validate output contract without inserting/updating provenance stamp.',
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
        policy_errors, policy_warnings = validate_policy(raw_graph, graph, enforce_dirty=True)
        for warning in policy_warnings:
            print(warning)
        if policy_errors:
            print('Policy validation failed:')
            for error in policy_errors:
                print(f'  - {error}')
            return 1
        print('Policy validation passed.')

    if is_execution_command:
        policy_errors, policy_warnings = validate_policy(
            raw_graph,
            graph,
            enforce_dirty=not args.allow_dirty,
            allow_dirty_override=args.allow_dirty,
        )
        for warning in policy_warnings:
            print(warning)
        if policy_errors:
            print('Policy validation failed:')
            for error in policy_errors:
                print(f'  - {error}')
            return 1
    elif is_listing_command and not args.validate_policy:
        # Listing commands are read-only: warn but do not refuse.
        policy_errors, policy_warnings = validate_policy(raw_graph, graph, enforce_dirty=False)
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
        preferred_order = get_task_preferred_order(raw_graph, args.task)
        routed_skills = order_skills_with_preference(graph, routed_skills, preferred_order)
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

    if args.validate_output:
        if not is_execution_command:
            print('Output validation failed:')
            print('  - --validate-output requires --task or --skill.')
            return 1
        execution_id = args.task if args.task else (args.skill or '')
        validation_errors = validate_output_file(
            output_path=args.validate_output,
            task_id=execution_id,
            model_id=args.model_id,
            affected_files=args.affected_files,
            raw_graph=raw_graph,
            stamp=not args.no_stamp,
        )
        if validation_errors:
            print('Output validation failed:')
            for error in validation_errors:
                print(f'  - {error}')
            return 1
        print(f'Output validation passed: {args.validate_output}')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
