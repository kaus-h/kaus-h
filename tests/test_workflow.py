import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "profile-metrics.yml"


class WorkflowTests(unittest.TestCase):
    def test_profile_metrics_workflow_has_required_triggers_and_generation(self):
        self.assertTrue(WORKFLOW.exists())
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("schedule:", text)
        self.assertIn("scripts/generate_profile.py", text)
        self.assertIn("GITHUB_TOKEN", text)
        self.assertIn("git diff --quiet", text)
        for metric in ("followers", "stars_received", "forks_received", "top_language"):
            self.assertIn(metric, text)


if __name__ == "__main__":
    unittest.main()
