import json
import os

# Store test results in memory
test_results = []
flaky_tests = {}

# Optional: Save test results to a JSON file for persistence
RESULTS_FILE = "test_results.json"

def load_results():
    """Load test results from JSON file (if exists)."""
    global test_results
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            test_results = json.load(f)

def save_results():
    """Save test results to JSON file."""
    with open(RESULTS_FILE, "w") as f:
        json.dump(test_results, f, indent=4)

# Load results at startup
load_results()
