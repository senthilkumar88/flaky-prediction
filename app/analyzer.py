import logging
from collections import defaultdict
from app.storage import test_results

logger = logging.getLogger("flaky_test_predictor")


class FlakyTestAnalyzer:
    def calculate_flakiness_score(self, test_name):
        """Calculate flakiness score based on memory-stored test results."""
        history = [t for t in test_results if t["test_name"] == test_name]
        if len(history) < 5:
            return 0.0  # Not enough data

        transitions = sum(1 for i in range(1, len(history)) if history[i]["status"] != history[i - 1]["status"])
        return transitions / (len(history) - 1) if len(history) > 1 else 0.0

    def detect_flaky_tests(self, threshold=0.2):
        """Detect flaky tests without using a database."""
        flaky_tests = {}

        test_names = set(t["test_name"] for t in test_results)
        for test_name in test_names:
            score = self.calculate_flakiness_score(test_name)
            if score >= threshold:
                flaky_tests[test_name] = score

        return flaky_tests
