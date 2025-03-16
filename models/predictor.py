import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from app.analyzer import FlakyTestAnalyzer
from app.storage import flaky_tests

MODEL_PATH = "flaky_test_model.pkl"

class FlakyTestPredictor:
    def train_model(self):
        """Train ML model on in-memory test data."""
        analyzer = FlakyTestAnalyzer()
        test_names = list(flaky_tests.keys())

        X, y = [], []
        for test_name in test_names:
            flaky_score = analyzer.calculate_flakiness_score(test_name)
            X.append([flaky_score])
            y.append(1 if flaky_score >= 0.2 else 0)

        if len(X) < 10:
            print("Not enough data to train model.")
            return False

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        print(classification_report(y_test, y_pred))

        joblib.dump(model, MODEL_PATH)
        return True
