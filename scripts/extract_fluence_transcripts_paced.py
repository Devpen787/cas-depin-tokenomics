#!/usr/bin/env python3
"""
Paced transcript extraction from youtube-transcript.io with minimal output format.

Outputs per video:
  - output/transcripts/<video_id>.md
  - output/transcripts/<video_id>.readable.md

Index:
  - output/transcripts/index.csv
"""

from __future__ import annotations

import argparse
import csv
import random
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from playwright.sync_api import sync_playwright


VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


@dataclass
class Config:
    repo_root: Path
    out_dir: Path
    index_path: Path
    user_data_dir: Path
    min_delay_s: int
    max_delay_s: int
    cooldown_every: int
    cooldown_s: int
    max_retries: int
    retry_base_s: int
    headless: bool
    skip_existing: bool
    paragraph_group: int
    page_wait_timeout_ms: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Paced transcript extraction runner.")
    parser.add_argument(
        "--video",
        action="append",
        default=[],
        help="YouTube video ID or URL. Can be provided multiple times.",
    )
    parser.add_argument(
        "--video-file",
        help="Path to newline-separated video IDs/URLs.",
    )
    parser.add_argument(
        "--repo-root",
        default="/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics",
        help="Repository root path.",
    )
    parser.add_argument("--min-delay-s", type=int, default=75)
    parser.add_argument("--max-delay-s", type=int, default=140)
    parser.add_argument("--cooldown-every", type=int, default=4)
    parser.add_argument("--cooldown-s", type=int, default=300)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--retry-base-s", type=int, default=45)
    parser.add_argument("--headless", action="store_true", default=True)
    parser.add_argument("--no-headless", dest="headless", action="store_false")
    parser.add_argument("--skip-existing", action="store_true", default=True)
    parser.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    parser.add_argument("--paragraph-group", type=int, default=25)
    parser.add_argument("--page-wait-timeout-ms", type=int, default=120000)
    return parser.parse_args()


def extract_video_id(raw: str) -> Optional[str]:
    raw = raw.strip()
    if not raw:
        return None
    if VIDEO_ID_RE.match(raw):
        return raw
    m = re.search(r"(?:v=|/videos\?id=|youtu\.be/)([A-Za-z0-9_-]{11})", raw)
    if m:
        return m.group(1)
    return None


def load_video_ids(cli_videos: list[str], video_file: Optional[str]) -> list[str]:
    ids: list[str] = []
    for v in cli_videos:
        vid = extract_video_id(v)
        if vid:
            ids.append(vid)

    if video_file:
        p = Path(video_file)
        if not p.exists():
            raise FileNotFoundError(f"Video file not found: {p}")
        for line in p.read_text(encoding="utf-8").splitlines():
            vid = extract_video_id(line)
            if vid:
                ids.append(vid)

    # Preserve order, remove duplicates.
    seen = set()
    out = []
    for vid in ids:
        if vid not in seen:
            seen.add(vid)
            out.append(vid)
    return out


def fmt_ts(sec_str: str) -> str:
    try:
        total = float(sec_str)
    except Exception:
        total = 0.0
    hrs = int(total // 3600)
    mins = int((total % 3600) // 60)
    secs = total % 60
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{secs:05.2f}"
    return f"{mins:02d}:{secs:05.2f}"


def ensure_index(path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "video_id",
        "title",
        "video_url",
        "source",
        "captured_at_utc",
        "language",
        "segment_count",
        "word_count_est",
        "transcript_path",
        "readable_path",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()


def upsert_index_row(index_path: Path, row: dict[str, str]) -> None:
    fields = [
        "video_id",
        "title",
        "video_url",
        "source",
        "captured_at_utc",
        "language",
        "segment_count",
        "word_count_est",
        "transcript_path",
        "readable_path",
    ]
    rows: list[dict[str, str]] = []
    if index_path.exists():
        with index_path.open("r", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("video_id") != row["video_id"]:
                    rows.append(r)
    rows.append(row)
    with index_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def write_outputs(cfg: Config, video_id: str, payload: dict[str, Any]) -> tuple[Path, Path, int, int, str]:
    entry = payload["success"][0]
    track = (entry.get("tracks") or [{}])[0]
    cues = track.get("transcript") or []
    if not cues:
        raise ValueError("Transcript track has no cues.")

    filtered: list[tuple[str, str]] = []
    timestamp_lines: list[str] = []
    for c in cues:
        txt = (c.get("text") or "").strip()
        if not txt:
            continue
        start = str(c.get("start", "0"))
        filtered.append((start, txt))
        timestamp_lines.append(f"[{fmt_ts(start)}] {txt}")

    full_text = " ".join(t for _, t in filtered)
    word_count = len(re.findall(r"\b\w+\b", full_text))
    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    title = entry.get("title", "(untitled)")
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    language = str(track.get("language") or "unknown")

    canonical = cfg.out_dir / f"{video_id}.md"
    canonical.write_text(
        "\n".join(
            [
                f"# {title}",
                "",
                f"- video_id: {video_id}",
                f"- video_url: {video_url}",
                "- source: youtube-transcript.io (/api/transcripts/v2)",
                f"- captured_at_utc: {captured_at}",
                f"- language: {language}",
                f"- segment_count: {len(cues)}",
                f"- word_count_est: {word_count}",
                "",
                "## Transcript (Timestamped)",
                *timestamp_lines,
            ]
        ),
        encoding="utf-8",
    )

    paragraphs: list[tuple[str, str, str]] = []
    for i in range(0, len(filtered), cfg.paragraph_group):
        chunk = filtered[i : i + cfg.paragraph_group]
        p = " ".join(t for _, t in chunk)
        p = re.sub(r"\s+([,.;:!?])", r"\1", p)
        p = re.sub(r"\s+", " ", p).strip()
        if p:
            paragraphs.append((fmt_ts(chunk[0][0]), fmt_ts(chunk[-1][0]), p))

    readable = cfg.out_dir / f"{video_id}.readable.md"
    readable_lines = [
        f"# {title}",
        "",
        f"- video_id: {video_id}",
        f"- video_url: {video_url}",
        "- source: youtube-transcript.io (/api/transcripts/v2)",
        f"- captured_at_utc: {captured_at}",
        f"- language: {language}",
        f"- segment_count: {len(cues)}",
        f"- word_count_est: {word_count}",
        "",
        "## Transcript (Readable)",
        "",
        f"- Paragraph grouping: {cfg.paragraph_group} cues per paragraph",
        "",
    ]
    for s, e, p in paragraphs:
        readable_lines.append(f"[{s} - {e}] {p}")
        readable_lines.append("")
    readable_lines += [
        "## Note",
        "- This companion file removes per-cue splitting for easier reading.",
        f"- Use `{canonical}` for timestamp-level citation evidence.",
    ]
    readable.write_text("\n".join(readable_lines), encoding="utf-8")

    upsert_index_row(
        cfg.index_path,
        {
            "video_id": video_id,
            "title": title,
            "video_url": video_url,
            "source": "youtube-transcript.io:/api/transcripts/v2",
            "captured_at_utc": captured_at,
            "language": language,
            "segment_count": str(len(cues)),
            "word_count_est": str(word_count),
            "transcript_path": str(canonical.relative_to(cfg.repo_root)),
            "readable_path": str(readable.relative_to(cfg.repo_root)),
        },
    )

    return canonical, readable, len(cues), word_count, title


def get_payload_for_video(page, video_id: str, timeout_s: int = 30) -> dict[str, Any]:
    holder: dict[str, Optional[dict[str, Any]]] = {"data": None}
    errors: list[str] = []

    def on_response(resp) -> None:
        if "/api/transcripts/v2" in resp.url and resp.status == 200:
            try:
                d = resp.json()
                s = d.get("success") if isinstance(d, dict) else None
                if isinstance(s, list) and s and isinstance(s[0], dict) and s[0].get("id") == video_id:
                    holder["data"] = d
            except Exception as e:
                errors.append(str(e))

    page.on("response", on_response)
    try:
        page.goto("https://www.youtube-transcript.io/", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(1500)
        page.locator('input[type="url"]').first.fill(f"https://www.youtube.com/watch?v={video_id}")
        page.locator('button:has-text("Extract transcript")').first.click()

        deadline = time.time() + timeout_s
        while time.time() < deadline and holder["data"] is None:
            page.wait_for_timeout(400)

        if holder["data"] is None:
            # Gather useful context before fail.
            body = page.locator("body").inner_text()[:1200]
            raise RuntimeError(f"Payload not received for {video_id}. Page snippet: {body}")
        return holder["data"]  # type: ignore[return-value]
    finally:
        page.remove_listener("response", on_response)


def maybe_sleep(seconds: int) -> None:
    if seconds <= 0:
        return
    print(f"Sleeping {seconds}s to pace requests...")
    time.sleep(seconds)


def run(cfg: Config, video_ids: list[str]) -> int:
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    ensure_index(cfg.index_path)

    processed = 0
    failures = 0

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(cfg.user_data_dir),
            headless=cfg.headless,
            viewport={"width": 1440, "height": 900},
        )
        page = ctx.new_page()

        for idx, video_id in enumerate(video_ids, start=1):
            canonical = cfg.out_dir / f"{video_id}.md"
            readable = cfg.out_dir / f"{video_id}.readable.md"
            if cfg.skip_existing and canonical.exists() and readable.exists():
                print(f"[{idx}/{len(video_ids)}] Skip existing {video_id}")
                continue

            print(f"[{idx}/{len(video_ids)}] Extracting {video_id} ...")
            ok = False
            for attempt in range(1, cfg.max_retries + 1):
                try:
                    payload = get_payload_for_video(page, video_id, timeout_s=35)
                    canonical_path, readable_path, segs, words, title = write_outputs(cfg, video_id, payload)
                    print(
                        f"Saved {video_id}: segs={segs} words={words}\n"
                        f"  - {canonical_path}\n"
                        f"  - {readable_path}\n"
                        f"  - title: {title}"
                    )
                    processed += 1
                    ok = True
                    break
                except Exception as e:
                    print(f"Attempt {attempt}/{cfg.max_retries} failed for {video_id}: {e}")
                    if attempt < cfg.max_retries:
                        backoff = cfg.retry_base_s * attempt + random.randint(5, 20)
                        maybe_sleep(backoff)
            if not ok:
                failures += 1
                print(f"FAILED: {video_id}")

            if idx < len(video_ids):
                pause = random.randint(cfg.min_delay_s, cfg.max_delay_s)
                maybe_sleep(pause)

            if cfg.cooldown_every > 0 and idx % cfg.cooldown_every == 0 and idx < len(video_ids):
                print(f"Cooldown after {idx} videos.")
                maybe_sleep(cfg.cooldown_s)

        ctx.close()

    print(f"Done. Processed={processed}, Failures={failures}, TotalRequested={len(video_ids)}")
    return 1 if failures else 0


def main() -> int:
    args = parse_args()
    if args.min_delay_s > args.max_delay_s:
        raise ValueError("--min-delay-s must be <= --max-delay-s")

    video_ids = load_video_ids(args.video, args.video_file)
    if not video_ids:
        print("No valid video IDs provided.")
        return 2

    repo_root = Path(args.repo_root).resolve()
    cfg = Config(
        repo_root=repo_root,
        out_dir=repo_root / "output" / "transcripts",
        index_path=repo_root / "output" / "transcripts" / "index.csv",
        user_data_dir=Path("/tmp/pw-ytio-profile"),
        min_delay_s=args.min_delay_s,
        max_delay_s=args.max_delay_s,
        cooldown_every=args.cooldown_every,
        cooldown_s=args.cooldown_s,
        max_retries=args.max_retries,
        retry_base_s=args.retry_base_s,
        headless=args.headless,
        skip_existing=args.skip_existing,
        paragraph_group=args.paragraph_group,
        page_wait_timeout_ms=args.page_wait_timeout_ms,
    )
    return run(cfg, video_ids)


if __name__ == "__main__":
    sys.exit(main())

