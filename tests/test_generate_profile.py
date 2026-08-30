import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from scripts.generate_profile import load_profile, render_telemetry, validate_profile

ROOT = Path(__file__).resolve().parents[1]


class ProfileGeneratorTests(unittest.TestCase):
    def test_profile_contains_required_flagship_metrics(self):
        profile = load_profile(ROOT / "data" / "profile.json")
        validate_profile(profile)

        projects = profile["projects"]
        self.assertEqual(projects["hydrascan"]["pose_hz"], 120)
        self.assertEqual(projects["hydrascan"]["landmarks"], 33)
        self.assertEqual(projects["hydrascan"]["metrics"], "50+")
        self.assertEqual(projects["patientconnect360"]["query_improvement"], "~95%")
        self.assertIn("beliefguard", projects)

    def test_render_telemetry_returns_parseable_svg_for_both_themes(self):
        profile = load_profile(ROOT / "data" / "profile.json")
        for theme in ("dark", "light"):
            svg = render_telemetry(profile, theme)
            root = ET.fromstring(svg)
            self.assertTrue(root.tag.endswith("svg"))
            self.assertIn("engineering telemetry", svg.lower())

    def test_required_theme_assets_exist_and_parse(self):
        for relative in (
            "assets/hero-dark.svg",
            "assets/hero-light.svg",
            "assets/telemetry-dark.svg",
            "assets/telemetry-light.svg",
        ):
            path = ROOT / relative
            self.assertTrue(path.exists(), relative)
            ET.parse(path)

    def test_flagship_project_assets_exist_and_parse(self):
        for project in ("hydrascan", "beliefguard", "patientconnect360"):
            for theme in ("dark", "light"):
                relative = f"assets/projects/{project}-{theme}.svg"
                asset = ROOT / relative
                self.assertTrue(asset.exists(), relative)
                ET.parse(asset)

    def test_render_telemetry_accepts_optional_live_metrics(self):
        profile = load_profile(ROOT / "data" / "profile.json")
        live = {
            "public_repositories": 24,
            "recent_commits": 17,
            "top_language": "TypeScript",
        }
        svg = render_telemetry(profile, "dark", live)
        self.assertIn("24", svg)
        self.assertIn("17", svg)
        self.assertIn("TypeScript", svg)

    def test_focus_rows_do_not_overlap_focus_heading(self):
        profile = load_profile(ROOT / "data" / "profile.json")
        root = ET.fromstring(render_telemetry(profile, "dark"))
        texts = {
            "".join(node.itertext()): float(node.attrib["y"])
            for node in root.iter()
            if node.tag.endswith("text") and "y" in node.attrib
        }
        self.assertGreaterEqual(texts["backend systems"] - texts["FOCUS / NOW"], 20)

    def test_dark_palette_uses_black_pink_green_and_light_blue(self):
        profile = load_profile(ROOT / "data" / "profile.json")
        svg = render_telemetry(profile, "dark")
        for color in ("#050509", "#FF4FD8", "#63F58B", "#7DD3FC"):
            self.assertIn(color, svg)

    def test_render_telemetry_supports_stat_max_live_metrics(self):
        profile = load_profile(ROOT / "data" / "profile.json")
        live = {
            "public_repositories": 24,
            "followers": 101,
            "stars_received": 55,
            "forks_received": 12,
            "recent_commits": 17,
            "top_language": "TypeScript",
        }
        svg = render_telemetry(profile, "dark", live)
        for value in ("24", "101", "55", "12", "17", "TypeScript"):
            self.assertIn(value, svg)

    def test_validate_profile_rejects_missing_required_project(self):
        profile = {
            "identity": {"name": "Kaustav Kalra"},
            "hero_stack": [],
            "projects": {},
            "focus": [],
            "stack": {},
        }
        with self.assertRaises(ValueError):
            validate_profile(profile)


if __name__ == "__main__":
    unittest.main()
