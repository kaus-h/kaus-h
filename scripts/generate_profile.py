from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path
from typing import Any

REQUIRED_PROJECTS = {"hydrascan", "beliefguard", "patientconnect360"}

PALETTES = {
    "dark": {
        "bg": "#050509",
        "panel": "#0B0F14",
        "panel_alt": "#111827",
        "text": "#F6FAFF",
        "muted": "#A7B0C0",
        "border": "#202634",
        "blue": "#7DD3FC",
        "pink": "#FF4FD8",
        "green": "#63F58B",
    },
    "light": {
        "bg": "#F7FAFC",
        "panel": "#FFFFFF",
        "panel_alt": "#F1F5F9",
        "text": "#09090B",
        "muted": "#4B5563",
        "border": "#D7DEE8",
        "blue": "#0284C7",
        "pink": "#C026D3",
        "green": "#16A34A",
    },
}


def load_profile(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_profile(profile: dict[str, Any]) -> None:
    required_top = {"identity", "hero_stack", "projects", "focus", "stack"}
    missing = required_top.difference(profile)
    if missing:
        raise ValueError(f"profile missing required keys: {sorted(missing)}")

    projects = profile.get("projects", {})
    missing_projects = REQUIRED_PROJECTS.difference(projects)
    if missing_projects:
        raise ValueError(f"profile missing required projects: {sorted(missing_projects)}")


def _pill(x: int, y: int, width: int, label: str, fill: str, text: str, border: str) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="34" rx="17" fill="{fill}" stroke="{border}"/>'
        f'<text x="{x + 16}" y="{y + 22}" class="mono tiny" fill="{text}">{escape(label)}</text>'
    )


def _metric(label: str, value: Any, x: int, y: int, color: str, p: dict[str, str]) -> str:
    safe = "—" if value in (None, "") else str(value)
    value_class = "metric compact" if len(safe) > 10 else "metric"
    return (
        f'<text x="{x}" y="{y}" class="mono label" fill="{p["muted"]}">{escape(label)}</text>'
        f'<text x="{x}" y="{y + 44}" class="sans {value_class}" fill="{color}">{escape(safe)}</text>'
    )


def render_telemetry(profile: dict[str, Any], theme: str, live_metrics: dict[str, Any] | None = None) -> str:
    validate_profile(profile)
    if theme not in PALETTES:
        raise ValueError(f"unsupported theme: {theme}")

    p = PALETTES[theme]
    focus = profile["focus"][:6]
    stack = profile["hero_stack"][:5]
    live = live_metrics or {}

    pills = []
    x = 70
    for label in stack:
        width = max(106, 34 + len(label) * 8)
        pills.append(_pill(x, 342, width, label.upper(), p["panel_alt"], p["text"], p["border"]))
        x += width + 12

    accents = (p["blue"], p["pink"], p["green"])
    focus_rows = []
    for i, label in enumerate(focus):
        y = 160 + i * 27
        focus_rows.append(
            f'<circle cx="784" cy="{y - 5}" r="4" fill="{accents[i % 3]}"/>'
            f'<text x="798" y="{y}" class="mono row" fill="{p["text"]}">{escape(label)}</text>'
        )

    metrics = [
        ("PUBLIC REPOS", live.get("public_repositories"), 72, 145, p["blue"]),
        ("FOLLOWERS", live.get("followers"), 272, 145, p["pink"]),
        ("STARS EARNED", live.get("stars_received"), 472, 145, p["green"]),
        ("FORKS", live.get("forks_received"), 72, 245, p["green"]),
        ("RECENT COMMITS", live.get("recent_commits"), 272, 245, p["blue"]),
        ("TOP LANGUAGE", live.get("top_language"), 472, 245, p["pink"]),
    ]
    metric_rows = [_metric(label, value, x0, y0, color, p) for label, value, x0, y0, color in metrics]

    status = "LIVE DATA" if live_metrics else "AUTO-REFRESH READY"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
<title id="title">Engineering telemetry</title>
<desc id="desc">A dense GitHub engineering telemetry panel using black, pink, green, and light blue accents.</desc>
<style>
.sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
.mono {{ font-family: SFMono-Regular, Consolas, "Liberation Mono", monospace; letter-spacing: 1.15px; }}
.kicker {{ font-size: 13px; font-weight: 800; }}
.label {{ font-size: 10px; font-weight: 800; }}
.row {{ font-size: 14px; font-weight: 650; }}
.tiny {{ font-size: 10px; font-weight: 800; }}
.metric {{ font-size: 33px; font-weight: 760; letter-spacing: -0.8px; }}
.compact {{ font-size: 22px; }}
</style>
<rect width="1200" height="400" rx="18" fill="{p['bg']}"/>
<rect x="1" y="1" width="1198" height="398" rx="17" fill="none" stroke="{p['border']}"/>
<text x="70" y="62" class="mono kicker" fill="{p['pink']}">ENGINEERING TELEMETRY / STAT MAX</text>
<circle cx="1034" cy="56" r="5" fill="{p['green']}"/>
<text x="1048" y="61" class="mono tiny" fill="{p['muted']}">{status}</text>
<path d="M70 84H1130" stroke="{p['border']}" stroke-dasharray="2 8"/>
{''.join(metric_rows)}
<rect x="736" y="108" width="394" height="214" rx="15" fill="{p['panel']}" stroke="{p['border']}"/>
<text x="782" y="132" class="mono label" fill="{p['blue']}">FOCUS / NOW</text>
{''.join(focus_rows)}
{''.join(pills)}
<path d="M1080 346 l6 -12 l6 12 l12 6 l-12 6 l-6 12 l-6 -12 l-12 -6 z" fill="{p['pink']}" opacity="0.95"/>
<circle cx="1038" cy="352" r="3" fill="{p['blue']}"/>
<circle cx="1054" cy="369" r="2.5" fill="{p['green']}"/>
<text x="742" y="363" class="mono tiny" fill="{p['muted']}">measure everything · polish what matters ♡</text>
</svg>'''


def render_activity(activity: dict[str, Any], theme: str) -> str:
    """Render a repo-owned 31-day public activity graph as SVG."""
    if theme not in PALETTES:
        raise ValueError(f"unsupported theme: {theme}")

    p = PALETTES[theme]
    items = sorted((str(day), max(0, int(count or 0))) for day, count in activity.items())[-31:]
    if not items:
        items = [("no-data", 0)]

    left, right = 80.0, 1120.0
    top, bottom = 96.0, 232.0
    chart_height = bottom - top
    peak_scale = max(1, max(count for _, count in items))
    step = (right - left) / max(1, len(items) - 1)

    points: list[tuple[float, float, str, int]] = []
    circles: list[str] = []
    for i, (day, count) in enumerate(items):
        x = left + step * i
        y = bottom - (count / peak_scale) * chart_height
        points.append((x, y, day, count))
        circles.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.5" fill="{p["green"]}" '
            f'stroke="{p["bg"]}" stroke-width="1.5"><title>{escape(day)}: {count}</title></circle>'
        )

    polyline = " ".join(f"{x:.2f},{y:.2f}" for x, y, _, _ in points)
    area_points = f"{points[0][0]:.2f},{bottom:.2f} {polyline} {points[-1][0]:.2f},{bottom:.2f}"

    grid: list[str] = []
    for i in range(4):
        y = top + (chart_height / 3) * i
        grid.append(
            f'<path d="M{left:.0f} {y:.2f}H{right:.0f}" stroke="{p["border"]}" stroke-dasharray="2 8"/>'
        )

    label_indexes = sorted({0, len(items) // 4, len(items) // 2, (len(items) * 3) // 4, len(items) - 1})
    labels: list[str] = []
    for idx in label_indexes:
        x, _, day, _ = points[idx]
        short = day[5:] if len(day) >= 10 else day
        labels.append(
            f'<text x="{x:.2f}" y="264" text-anchor="middle" class="mono axis" fill="{p["muted"]}">{escape(short)}</text>'
        )

    total = sum(count for _, count in items)
    active_days = sum(1 for _, count in items if count)
    peak = max(count for _, count in items)
    first_day = items[0][0]
    last_day = items[-1][0]

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-labelledby="title desc">
<title id="title">Recent public activity</title>
<desc id="desc">Repo-owned GitHub activity graph from {escape(first_day)} through {escape(last_day)}.</desc>
<style>
.sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
.mono {{ font-family: SFMono-Regular, Consolas, "Liberation Mono", monospace; letter-spacing: 1px; }}
.kicker {{ font-size: 13px; font-weight: 800; }}
.axis {{ font-size: 10px; font-weight: 700; }}
.stat {{ font-size: 11px; font-weight: 800; }}
</style>
<rect width="1200" height="300" rx="18" fill="{p['bg']}"/>
<rect x="1" y="1" width="1198" height="298" rx="17" fill="none" stroke="{p['border']}"/>
<text x="70" y="48" class="mono kicker" fill="{p['pink']}">RECENT PUBLIC ACTIVITY / 31 DAYS</text>
<circle cx="1017" cy="43" r="4.5" fill="{p['green']}"/>
<text x="1031" y="48" class="mono stat" fill="{p['muted']}">REPO-OWNED SVG</text>
{''.join(grid)}
<polygon points="{area_points}" fill="{p['blue']}" opacity="0.12"/>
<polyline points="{polyline}" fill="none" stroke="{p['pink']}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
{''.join(circles)}
{''.join(labels)}
<text x="80" y="286" class="mono stat" fill="{p['blue']}">TOTAL {total}</text>
<text x="190" y="286" class="mono stat" fill="{p['green']}">ACTIVE DAYS {active_days}</text>
<text x="350" y="286" class="mono stat" fill="{p['pink']}">PEAK {peak}</text>
<text x="1120" y="286" text-anchor="end" class="mono stat" fill="{p['muted']}">no external renderer · no sad broken image ♡</text>
<path d="M1090 44 l5 -10 l5 10 l10 5 l-10 5 l-5 10 l-5 -10 l-10 -5 z" fill="{p['blue']}" opacity="0.9"/>
</svg>'''


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GitHub profile SVG assets")
    parser.add_argument("--profile", type=Path, default=Path("data/profile.json"))
    parser.add_argument("--theme", choices=sorted(PALETTES), required=True)
    parser.add_argument("--kind", choices=("telemetry", "activity"), default="telemetry")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--github-json", type=Path)
    args = parser.parse_args()

    profile = load_profile(args.profile)
    live_metrics = load_profile(args.github_json) if args.github_json else None
    if args.kind == "activity":
        activity = (live_metrics or {}).get("activity", {})
        svg = render_activity(activity, args.theme)
    else:
        svg = render_telemetry(profile, args.theme, live_metrics)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
