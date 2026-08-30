import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class ReadmeContentTests(unittest.TestCase):
    def setUp(self):
        self.text = README.read_text(encoding="utf-8")

    def test_preserves_substantive_original_facts(self):
        required = [
            "Arizona State University",
            "95%",
            "RBAC",
            "MPOA",
            "Repo Belief Graph",
            "Confidence-to-Action Gate",
            "120Hz",
            "33-point",
            "50+",
            "12K+",
            "700+",
            "Redis",
            "76 percent",
            "iDTech",
            "On My Own Technology",
            "IndianRaga",
            "https://www.linkedin.com/in/kaustavkalra/",
            "https://github.com/kaus-h",
        ]
        for value in required:
            with self.subTest(value=value):
                self.assertIn(value, self.text)

    def test_embeds_theme_aware_hero_and_flagship_cards(self):
        required_assets = [
            "./assets/hero-dark.svg",
            "./assets/hero-light.svg",
            "./assets/projects/hydrascan-dark.svg",
            "./assets/projects/hydrascan-light.svg",
            "./assets/projects/beliefguard-dark.svg",
            "./assets/projects/beliefguard-light.svg",
            "./assets/projects/patientconnect360-dark.svg",
            "./assets/projects/patientconnect360-light.svg",
        ]
        for asset in required_assets:
            self.assertIn(asset, self.text)
            self.assertTrue((ROOT / asset.removeprefix("./")).exists(), asset)

    def test_stat_max_widgets_are_visible(self):
        required = [
            "github-stats-extended.vercel.app/api?username=kaus-h",
            "github-stats-extended.vercel.app/api/top-langs/?username=kaus-h",
            "streak-stats.demolab.com",
            "github-readme-activity-graph.vercel.app/graph?username=kaus-h",
            "img.shields.io/github/followers/kaus-h",
        ]
        for value in required:
            self.assertIn(value, self.text)

    def test_activity_graph_uses_documented_linked_markdown_pattern(self):
        self.assertIn(
            "[![Kaustav's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=kaus-h",
            self.text,
        )
        self.assertIn(
            "](https://github.com/ashutosh00710/github-readme-activity-graph)",
            self.text,
        )
        self.assertNotIn(
            '<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=kaus-h',
            self.text,
        )

    def test_hero_centers_lowercase_identity_and_removes_tagline(self):
        for name in ("hero-dark.svg", "hero-light.svg"):
            hero = (ROOT / "assets" / name).read_text(encoding="utf-8")
            with self.subTest(name=name):
                self.assertIn('x="600"', hero)
                self.assertIn('text-anchor="middle"', hero)
                self.assertIn('>kaustav kalra</text>', hero)
                self.assertIn('>software engineer · systems + design</text>', hero)
                self.assertNotIn('building across the layers people see', hero)
                self.assertNotIn("and the systems they shouldn't have to think about.", hero)
                self.assertNotIn('>KAUSTAV KALRA</text>', hero)

    def test_readme_uses_black_pink_green_light_blue_palette(self):
        for color in ("050509", "FF4FD8", "63F58B", "7DD3FC"):
            self.assertIn(color, self.text)

    def test_all_local_svg_references_exist(self):
        refs = set(re.findall(r'(?:src|srcset)="(\./assets/[^"]+\.svg)"', self.text))
        self.assertGreaterEqual(len(refs), 10)
        for ref in refs:
            self.assertTrue((ROOT / ref.removeprefix("./")).exists(), ref)


if __name__ == "__main__":
    unittest.main()
