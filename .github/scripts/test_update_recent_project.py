import unittest
import http.client
import io
from datetime import datetime, timezone
from unittest.mock import patch

from update_recent_project import (
    calculate_project_score,
    clean_card_text,
    fetch_json,
    is_documentation_commit,
    is_excluded_project,
)


class RecentProjectSelectionTests(unittest.TestCase):
    def test_documentation_and_repository_housekeeping_do_not_count_as_activity(self):
        self.assertTrue(is_documentation_commit("docs: add project README"))
        self.assertTrue(is_documentation_commit("Add gitignore and remove node_modules"))
        self.assertFalse(is_documentation_commit("feat: complete hospital website"))

    def test_practice_repositories_are_not_featured(self):
        self.assertTrue(is_excluded_project("daily-_leetcode", "anurohan"))
        self.assertTrue(is_excluded_project("Basic-to-advanve-java", "anurohan"))
        self.assertTrue(is_excluded_project("anurohan", "anurohan"))
        self.assertFalse(is_excluded_project("hospital", "anurohan"))

    def test_card_text_removes_markdown_and_truncates_at_word_boundary(self):
        self.assertEqual(
            clean_card_text("**A useful project description**", 40),
            "A useful project description",
        )
        self.assertEqual(
            clean_card_text("A useful project description for the profile", 24),
            "A useful project…",
        )

    def test_recent_code_updates_rank_above_old_updates(self):
        project = {
            "size": 200,
            "description": "Patient management system",
            "language": "TypeScript",
            "homepage": "https://example.com",
            "topics": ["healthcare", "nextjs"],
            "stargazers_count": 2,
            "forks_count": 1,
        }
        now = datetime(2026, 10, 15, tzinfo=timezone.utc)
        recent_score = calculate_project_score(project, "2026-10-12T00:00:00Z", now)
        old_score = calculate_project_score(project, "2026-04-12T00:00:00Z", now)

        self.assertGreater(recent_score, old_score)

    def test_recent_project_can_beat_a_more_popular_but_stale_project(self):
        recent_project = {
            "size": 200,
            "description": "Patient management system",
            "language": "TypeScript",
            "stargazers_count": 2,
        }
        deployed_project = {
            **recent_project,
            "size": 249,
            "homepage": "https://example.com",
        }
        now = datetime(2026, 10, 15, tzinfo=timezone.utc)
        recent_score = calculate_project_score(
            recent_project, "2026-10-12T00:00:00Z", now
        )
        deployed_score = calculate_project_score(
            deployed_project, "2026-09-26T00:00:00Z", now
        )

        self.assertGreater(recent_score, deployed_score)

    @patch("update_recent_project.time.sleep")
    @patch("update_recent_project.urllib.request.urlopen")
    def test_api_fetch_retries_an_incomplete_response(self, urlopen, sleep):
        urlopen.side_effect = [
            http.client.IncompleteRead(b"{", 1),
            io.BytesIO(b'{"ok": true}'),
        ]

        self.assertEqual(fetch_json("https://api.github.com/test"), {"ok": True})
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1)


if __name__ == "__main__":
    unittest.main()
