import logging
from datetime import datetime
from app.storage import test_results, save_results

logger = logging.getLogger("flaky_test_predictor")

class TestResultCollector:
    def process_test_results(self, test_data):
        """Process and store test results from any framework (JUnit, Selenium, ITAF)."""
        
        if "framework" not in test_data:
            return {"error": "Framework not specified"}, 400

        valid_frameworks = ["JUnit", "Selenium", "ITAF"]
        if test_data["framework"] not in valid_frameworks:
            return {"error": "Unsupported test framework"}, 400

        test_results.append(test_data)  # Store results in memory
        save_results()  # Persist results

        return {"success": True}

