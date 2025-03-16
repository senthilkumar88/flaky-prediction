# 🚀 Flaky Test Predictor

A **Flaky Test Predictor** that detects and predicts **flaky tests** across different test automation frameworks such as **JUnit, Selenium, ITAF**. It provides a **real-time dashboard**, supports **machine learning-based flakiness prediction**, and integrates with **CI/CD pipelines** for scalable deployment.

---

## **📌 Features**
✅ **Detect flaky tests dynamically** based on test history  
✅ **Supports JUnit, Selenium, ITAF** (Easily extendable for more frameworks)  
✅ **Machine Learning (RandomForestClassifier)** predicts flaky tests  
✅ **Live Dashboard (`/results`)** for real-time monitoring  
✅ **Secure API** with input validation  
✅ **CI/CD Integration** (Runs inside GitHub Actions, Jenkins)  
✅ **Scalable Deployment** using **Docker + Azure**  

---

## **🛠️ Architecture Overview**
### **🚀 High-Level Architecture**
```
┌──────────────┐       ┌──────────────┐       ┌────────────────────┐
│  Test Tools  │ ───→  │  Flask API   │ ───→  │ ML Model (RandomForest) │
│ (JUnit, Selenium, ITAF) │  │   Python + SQLite  │  │  Predicts Flaky Tests │
└──────────────┘       └──────────────┘       └────────────────────┘
                              │
                              ↓
                     ┌────────────────┐
                     │  Dashboard UI  │
                     │  (Bootstrap)   │
                     └────────────────┘
```

- **Test frameworks** send results to the **Flask API**.  
- API **stores test results** and **calculates flakiness scores**.  
- The **ML model** detects flaky tests.  
- A **real-time dashboard** visualizes flaky test data.

---

## **📂 Folder Structure**
```
flaky-test-predictor/
│── app/
│   │── __init__.py         # Flask App Initialization
│   │── routes.py           # API Routes
│   │── collector.py        # Handles test result storage
│   │── analyzer.py         # Flakiness analysis logic
│   │── storage.py          # Stores test results in memory
│
│── models/
│   │── predictor.py        # ML Model Training & Prediction
│   │── flaky_test_model.pkl  # Trained ML Model (Generated)
│
│── templates/
│   │── results.html        # Frontend UI for reports
│
│── static/                 # (CSS/JS if needed)
│── tests/                  # Unit Tests for API
│── run.py                  # Main Flask App Entry Point
│── requirements.txt         # Dependencies
│── Dockerfile               # Docker Container Setup
│── README.md               # Documentation
```

---

## **🚀 Installation Guide**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/flaky-test-predictor.git
cd flaky-test-predictor
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows**:
  ```bash
  venv\Scriptsctivate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
python run.py
```
✅ The Flask app will start on:
```
http://127.0.0.1:5000/
```

---

## **📊 Using the API**
### **1️⃣ Insert Test Results**
```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/import-results" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"test_name": "test_login", "test_file": "test_auth.py", "test_class": "TestLogin", "duration": 1.2, "status": "PASS", "error_message": null, "environment": "staging", "framework": "JUnit"}'
```
✅ This adds a **test execution record**.

### **2️⃣ Get Flaky Test Analysis**
```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/flaky-tests" -Method GET
```
✅ **Detects flaky tests** based on historical data.

### **3️⃣ Train & Predict ML Model**
```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/run-prediction" -Method GET
```
✅ **Predicts flaky tests** using **Machine Learning**.

### **4️⃣ View the Results Dashboard**
Open your browser:
```
http://127.0.0.1:5000/results
```
✅ **Live test execution reports** 📊.

---

## **🚀 Running Inside Docker**
### **1️⃣ Build the Docker Image**
```bash
docker build -t flaky-test-predictor .
```

### **2️⃣ Run the Container**
```bash
docker run -p 5000:5000 flaky-test-predictor
```
✅ **Now your app runs inside a Docker container!**

---

## **🔗 CI/CD Integration (GitHub Actions)**
### **📂 `.github/workflows/test-suite.yml`**
```yaml
name: Run API Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: "3.9"

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run API Tests
        run: pytest tests/
```
✅ **This ensures tests run automatically in CI/CD!**

---

## **🔒 Security Best Practices**
✅ **Sanitize Inputs**: Prevents SQL Injection  
✅ **API Rate Limiting**: Protects from abuse  
✅ **HTTPS Deployment**: Ensures encrypted connections  

---

## **🚀 Deployment on Azure**
1️⃣ **Push Docker Image to Azure**
```bash
az webapp create --resource-group MyResourceGroup --plan MyAppPlan --name flaky-test-api --deployment-container-image-name flaky-test-predictor
```
2️⃣ **Enable Auto-Scaling** in Azure App Service.

✅ **Now your app is cloud-deployed!** 🌍

---

## **👨‍💻 Contributing**
We welcome contributions! Fork this repo, make improvements, and submit a PR.

---

## **📝 License**
MIT License - Use this freely.

---

## **🎯 Summary**
| **Feature** | **Description** |
|------------|---------------|
| **Test Frameworks** | Supports **JUnit, Selenium, ITAF** |
| **Flaky Test Detection** | Detects flaky tests dynamically |
| **ML Predictions** | Uses **RandomForest** for flaky test predictions |
| **Live Dashboard** | Shows **real-time test reports** |
| **CI/CD Ready** | Runs in **GitHub Actions / Jenkins** |
| **Dockerized** | Deploys with **Docker & Azure** |
| **Security** | **Input validation, HTTPS support** |

---

