🚀 Executing Positive & Negative Test Scenarios
Now that Invoke-WebRequest works for you, let’s test both positive (expected behavior) and negative (error handling) scenarios for your Flaky Test Predictor API.

✅ 1. Positive Test Cases
These will confirm that your API works correctly.

1️⃣ Insert Valid Test Results (Positive)
Expected: The API should accept test results and return {"success": true}.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/import-results" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"test_name": "test_login", "test_file": "test_auth.py", "test_class": "TestLogin", "duration": 1.2, "status": "PASS", "error_message": null, "environment": "staging", "framework": "pytest"}'
✅ Expected Output (Success):

json
Copy
Edit
{"success": true}
2️⃣ Retrieve Flaky Test Analysis (Positive)
Once multiple test results are inserted (some PASS, some FAIL), check for flaky tests.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/flaky-tests" -Method GET
✅ Expected Output (if tests are flaky):

json
Copy
Edit
{
    "test_login": 0.5
}
(A score above 0.2 indicates flakiness.)

3️⃣ Run ML Model Prediction (Positive)
Train and run the ML model on test history.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/run-prediction" -Method GET
✅ Expected Output (Example)

json
Copy
Edit
[
    {
        "test_name": "test_login",
        "flaky_probability": 0.75,
        "features": {
            "avg_duration": 1.35,
            "duration_variance": 0.1,
            "fail_rate": 0.5,
            "environment_count": 1,
            "has_assertions": false,
            "has_async": false
        }
    }
]
(A high probability > 0.5 means the test is likely flaky.)

❌ 2. Negative Test Cases
These will test how well your API handles errors.

4️⃣ Insert Test Without test_name (Negative)
Expected: API should reject the request with a 400 Bad Request.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/import-results" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"test_file": "test_auth.py", "test_class": "TestLogin", "duration": 1.2, "status": "PASS", "error_message": null, "environment": "staging", "framework": "pytest"}'
❌ Expected Error:

json
Copy
Edit
{"error": "Missing test_name"}
5️⃣ Insert Test with Invalid JSON (Negative)
Expected: API should return an error for incorrect JSON format.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/import-results" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{test_name: "test_login" test_file: "test_auth.py" duration: 1.2}'
❌ Expected Error:

javascript
Copy
Edit
400 Bad Request - Invalid JSON
6️⃣ Check Flaky Tests When No Data Exists (Negative)
Expected: API should return an empty result if no test history exists.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/flaky-tests" -Method GET
❌ Expected Output:

json
Copy
Edit
{}
(This means no flaky tests were detected.)

7️⃣ Train ML Model Without Data (Negative)
Expected: API should return an error if no test history exists.

powershell
Copy
Edit
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/run-prediction" -Method GET
❌ Expected Output:

json
Copy
Edit
{"error": "Insufficient data to train model"}
🎯 Summary of Test Scenarios
Test Case	Command	Expected Result
Insert valid test result ✅	/api/import-results (POST)	{"success": true}
Check flaky tests with history ✅	/api/flaky-tests (GET)	{"test_login": 0.5}
Train ML model ✅	/api/run-prediction (GET)	{"flaky_probability": 0.75}
Insert test without test_name ❌	/api/import-results (POST)	{"error": "Missing test_name"}
Insert malformed JSON ❌	/api/import-results (POST)	400 Bad Request
Check flaky tests with no history ❌	/api/flaky-tests (GET)	{}
Train model with no data ❌	/api/run-prediction (GET)	{"error": "Insufficient data"}
