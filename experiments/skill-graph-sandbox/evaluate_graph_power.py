#!/usr/bin/env python3
"""Compare baseline checks vs graph-routed checks on sandbox text."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / '.agent' / 'knowledge-skill-graph.json'

sys.path.insert(0, str(ROOT / 'scripts'))
import knowledge_skill_graph as ksg  # noqa: E402


@dataclass(frozen=True)
class Finding:
    detector: str
    line: int
    message: str
    excerpt: str


Detector = Callable[[Sequence[str]], List[Finding]]


def detect_lexicon_drift(lines: Sequence[str]) -> List[Finding]:
    findings: List[Finding] = []
    pattern = re.compile(r'\bORSTE\b')
    for idx, line in enumerate(lines, start=1):
        if pattern.search(line):
            findings.append(
                Finding(
                    detector='lexicon-drift',
                    line=idx,
                    message='Found banned term ORSTE; use DTSE instead.',
                    excerpt=line.strip(),
                ),
            )
    return findings


def detect_citation_gaps(lines: Sequence[str]) -> List[Finding]:
    findings: List[Finding] = []
    claim_pattern = re.compile(r'\b(according to|stud(?:y|ies)|research|evidence)\b', re.IGNORECASE)
    citation_pattern = re.compile(r'\\cite\{[^}]+\}|% TODO-CITE:', re.IGNORECASE)
    for idx, line in enumerate(lines, start=1):
        if claim_pattern.search(line) and not citation_pattern.search(line):
            findings.append(
                Finding(
                    detector='citation-gap',
                    line=idx,
                    message='Claim-like statement without cite or TODO-CITE marker.',
                    excerpt=line.strip(),
                ),
            )
    return findings


def detect_unresolved_todo_cite(lines: Sequence[str]) -> List[Finding]:
    findings: List[Finding] = []
    pattern = re.compile(r'%\s*TODO-CITE:', re.IGNORECASE)
    for idx, line in enumerate(lines, start=1):
        if pattern.search(line):
            findings.append(
                Finding(
                    detector='unresolved-todo-cite',
                    line=idx,
                    message='Unresolved TODO-CITE remains in draft.',
                    excerpt=line.strip(),
                ),
            )
    return findings


def detect_overclaiming(lines: Sequence[str]) -> List[Finding]:
    findings: List[Finding] = []
    pattern = re.compile(
        r'\b(always|never|guarantee(?:s|d)?|prove(?:s|d)?|certain(?:ly)?|with certainty)\b',
        re.IGNORECASE,
    )
    for idx, line in enumerate(lines, start=1):
        if pattern.search(line):
            findings.append(
                Finding(
                    detector='overclaiming',
                    line=idx,
                    message='Absolute language may overstate certainty.',
                    excerpt=line.strip(),
                ),
            )
    return findings


def detect_scope_contract(lines: Sequence[str]) -> List[Finding]:
    first_window = lines[:40]
    for line in first_window:
        if '% SCOPE CONTRACT:' in line:
            return []
    return [
        Finding(
            detector='scope-contract',
            line=1,
            message='Missing % SCOPE CONTRACT declaration near top of file.',
            excerpt=lines[0].strip() if lines else '',
        ),
    ]


def detect_golden_thread_alignment(lines: Sequence[str]) -> List[Finding]:
    text = '\n'.join(lines).lower()
    keywords = [
        'bme',
        'capped supply',
        'stress',
        'robustness',
        'catastrophic failure',
        'dtse',
    ]
    matched = [term for term in keywords if term in text]
    if len(matched) >= 2:
        return []
    return [
        Finding(
            detector='golden-thread',
            line=1,
            message='Section appears weakly connected to core thesis question terms.',
            excerpt=lines[0].strip() if lines else '',
        ),
    ]


def detect_metric_definition(lines: Sequence[str]) -> List[Finding]:
    findings: List[Finding] = []
    metrics = ['churn_ratio', 'resilience_index', 'burn_to_mint_ratio', 'provider_opex']
    lower_lines = [line.lower() for line in lines]

    defined: Set[str] = set()
    for metric in metrics:
        definition_pattern = re.compile(rf'\b{re.escape(metric.lower())}\b.*\bdefined as\b')
        if any(definition_pattern.search(line) for line in lower_lines):
            defined.add(metric)

    seen_flagged: Set[str] = set()
    for idx, line in enumerate(lower_lines, start=1):
        for metric in metrics:
            if metric in line and metric not in defined and metric not in seen_flagged:
                findings.append(
                    Finding(
                        detector='metric-definition',
                        line=idx,
                        message=f'Metric "{metric}" appears without an explicit definition.',
                        excerpt=lines[idx - 1].strip(),
                    ),
                )
                seen_flagged.add(metric)
    return findings


DETECTORS: Dict[str, Detector] = {
    'lexicon-drift': detect_lexicon_drift,
    'citation-gap': detect_citation_gaps,
    'unresolved-todo-cite': detect_unresolved_todo_cite,
    'overclaiming': detect_overclaiming,
    'scope-contract': detect_scope_contract,
    'golden-thread': detect_golden_thread_alignment,
    'metric-definition': detect_metric_definition,
}

SKILL_TO_DETECTORS: Dict[str, List[str]] = {
    'skill.lexicon-guard-dtse': ['lexicon-drift'],
    'skill.citation-gap-tagging': ['citation-gap'],
    'skill.reference-resolution': ['unresolved-todo-cite'],
    'skill.hostile-review': ['overclaiming'],
    'skill.results-interpretation-guard': ['overclaiming'],
    'skill.scope-contract-check': ['scope-contract'],
    'skill.golden-thread-alignment': ['golden-thread'],
    'skill.metric-definition-audit': ['metric-definition'],
}

# Baseline intentionally mimics a simple "single-skill" generic pass.
BASELINE_DETECTORS = ['citation-gap', 'overclaiming']


def run_detectors(detector_ids: Sequence[str], lines: Sequence[str]) -> List[Finding]:
    findings: List[Finding] = []
    seen: Set[Tuple[str, int, str]] = set()
    for detector_id in detector_ids:
        detector = DETECTORS[detector_id]
        for finding in detector(lines):
            key = (finding.detector, finding.line, finding.message)
            if key in seen:
                continue
            seen.add(key)
            findings.append(finding)
    return sorted(findings, key=lambda item: (item.line, item.detector))


def render_findings(title: str, findings: Sequence[Finding]) -> None:
    print(title)
    if not findings:
        print('  - No findings.')
        return
    for finding in findings:
        print(
            f'  - L{finding.line:03d} [{finding.detector}] {finding.message} :: {finding.excerpt}',
        )


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(
        description='Evaluate graph-routed checks on synthetic thesis-like content.',
    )
    parser.add_argument(
        '--task',
        type=str,
        default='task.pre-submission-review',
        help='Task id from the knowledge-skill graph.',
    )
    parser.add_argument(
        '--input',
        type=Path,
        default=ROOT / 'experiments' / 'skill-graph-sandbox' / 'corpus' / 'mock_results_section.tex',
        help='Path to synthetic input file.',
    )
    parser.add_argument(
        '--graph',
        type=Path,
        default=GRAPH_PATH,
        help='Path to the graph JSON.',
    )
    args = parser.parse_args(argv)

    if not args.input.exists():
        print(f'Input file not found: {args.input}')
        return 1

    graph = ksg.load_graph(args.graph)
    errors = ksg.validate_graph(graph)
    if errors:
        print('Graph validation failed. Fix graph before sandbox evaluation:')
        for error in errors:
            print(f'  - {error}')
        return 1

    routed_skills = ksg.collect_task_skills(graph, args.task)
    graph_detector_ids = sorted(
        {
            detector_id
            for skill_id in routed_skills
            for detector_id in SKILL_TO_DETECTORS.get(skill_id, [])
        },
    )

    lines = args.input.read_text(encoding='utf-8').splitlines()
    baseline_findings = run_detectors(BASELINE_DETECTORS, lines)
    graph_findings = run_detectors(graph_detector_ids, lines)

    print(f'Knowledge graph: {args.graph}')
    print(f'Task: {args.task}')
    print('Routed skills:')
    for idx, skill_id in enumerate(routed_skills, start=1):
        skill_name = graph.nodes[skill_id].name
        print(f'  {idx}. {skill_id} - {skill_name}')
    print()
    print(f'Baseline detectors: {", ".join(BASELINE_DETECTORS)}')
    print(f'Graph detectors: {", ".join(graph_detector_ids) if graph_detector_ids else "(none)"}')
    print()

    render_findings('Baseline findings', baseline_findings)
    print()
    render_findings('Graph-routed findings', graph_findings)
    print()

    uplift = len(graph_findings) - len(baseline_findings)
    print('Summary')
    print(f'  Baseline findings: {len(baseline_findings)}')
    print(f'  Graph findings:    {len(graph_findings)}')
    print(f'  Uplift:            {uplift:+d}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
