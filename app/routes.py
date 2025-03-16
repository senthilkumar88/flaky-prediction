from flask import request, jsonify, render_template
from app.analyzer import FlakyTestAnalyzer
from app.collector import TestResultCollector
from app.storage import test_results

def register_routes(app):
    @app.route("/")
    def home():
        return "<h1>Flaky Test Predictor API is Running!</h1>"

    @app.route("/results")
    def results():
        """Render the results screen."""
        return render_template("results.html")

    @app.route("/api/import-results", methods=["POST"])
    def import_results():
        """Insert test execution data."""
        data = request.json
        if not data.get("test_name"):
            return jsonify({"error": "Missing test_name"}), 400

        collector = TestResultCollector()
        collector.process_test_results(data)
        return jsonify({"success": True})

    @app.route("/api/flaky-tests", methods=["GET"])
    def get_flaky_tests():
        """Retrieve flaky test analysis."""
        analyzer = FlakyTestAnalyzer()
        return jsonify(analyzer.detect_flaky_tests())

    @app.route("/api/test-history", methods=["GET"])
    def get_test_history():
        """Retrieve all test execution history."""
        return jsonify(test_results)
