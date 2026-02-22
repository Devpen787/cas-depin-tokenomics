#!/usr/bin/env python3
"""Generate deterministic topology snapshot for graph regression checks."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Dict, List


DEFAULT_GRAPH_PATH = Path('.agent/knowledge-skill-graph.json')
DEFAULT_OUTPUT_PATH = Path('scripts/regression_expected/graph_topology_snapshot.json')


def sorted_counter(counter: Counter[str]) -> Dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def build_snapshot(graph_data: Dict[str, object]) -> Dict[str, object]:
    raw_nodes = graph_data.get('nodes', [])
    raw_edges = graph_data.get('edges', [])

    nodes: List[Dict[str, object]] = [item for item in raw_nodes if isinstance(item, dict)]
    edges: List[Dict[str, object]] = [item for item in raw_edges if isinstance(item, dict)]

    nodes_by_type = Counter(
        str(node.get('type', 'unknown'))
        for node in nodes
    )
    edges_by_type = Counter(
        str(edge.get('type', 'unknown'))
        for edge in edges
    )

    edge_triples = sorted(
        f"{edge.get('source', '')}|{edge.get('type', '')}|{edge.get('target', '')}"
        for edge in edges
    )
    fingerprint_input = '\n'.join(edge_triples).encode('utf-8')
    fingerprint = hashlib.sha256(fingerprint_input).hexdigest()

    return {
        'nodes_total': len(nodes),
        'edges_total': len(edges),
        'nodes_by_type': sorted_counter(nodes_by_type),
        'edges_by_type': sorted_counter(edges_by_type),
        'edges_fingerprint': fingerprint,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Generate graph topology snapshot JSON.')
    parser.add_argument(
        '--graph',
        type=Path,
        default=DEFAULT_GRAPH_PATH,
        help=f'Graph JSON path (default: {DEFAULT_GRAPH_PATH})',
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f'Snapshot output path (default: {DEFAULT_OUTPUT_PATH})',
    )
    args = parser.parse_args()

    graph_data = json.loads(args.graph.read_text(encoding='utf-8'))
    snapshot = build_snapshot(graph_data)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(snapshot, indent=2, sort_keys=True) + '\n',
        encoding='utf-8',
    )
    print(f'Wrote topology snapshot to {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
