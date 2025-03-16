import os

# Database path
DB_PATH = os.path.join(os.getcwd(), "data", "test_results.db")

# Model path
MODEL_PATH = os.path.join(os.getcwd(), "models", "flaky_test_model.pkl")

# Flakiness detection threshold
FLAKY_THRESHOLD = 0.2