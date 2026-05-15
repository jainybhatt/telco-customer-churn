import requests

BASE_URL = "http://localhost:8000"
API_KEY = "test-key-123"
HEADERS = {"Content-Type": "application/json", "X-API-KEY": API_KEY}

# ------- Health --------

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"
    assert r.json()["model_loaded"] == True

#  ------- Auth --------

def test_predict_no_key():
    r = requests.post(f"{BASE_URL}/predict", 
                      json={
                            "Gender": "Female",
                            "SeniorCitizen": 0,
                            "Partner": "Yes",
                            "Dependents": "No",
                            "Tenure": 25,
                            "PhoneService": "Yes",
                            "MultipleLines": "Yes",
                            "InternetService": "Yes",
                            "OnlineSecurity": "Yes",
                            "OnlineBackup": "No",
                            "DeviceProtection": "No",
                            "TechSupport": "No",
                            "StreamingTV": "Yes",
                            "StreamingMovies": "Yes",
                            "Contract": "1-year",
                            "PaperlessBilling": "Yes",
                            "PaymentMethod": "Bank transfer",
                            "MonthlyCharges": 80.45,
                            "TotalCharges": 90.23
                        })
    assert r.status_code == 401

def test_predict_wrong_key():
    r = requests.post(f"{BASE_URL}/predict", 
                      headers={"X-API-Key": "wrong"},
                      json={
                            "Gender": "Female",
                            "SeniorCitizen": 0,
                            "Partner": "Yes",
                            "Dependents": "No",
                            "Tenure": 25,
                            "PhoneService": "Yes",
                            "MultipleLines": "Yes",
                            "InternetService": "Yes",
                            "OnlineSecurity": "Yes",
                            "OnlineBackup": "No",
                            "DeviceProtection": "No",
                            "TechSupport": "No",
                            "StreamingTV": "Yes",
                            "StreamingMovies": "Yes",
                            "Contract": "1-year",
                            "PaperlessBilling": "Yes",
                            "PaymentMethod": "Bank transfer",
                            "MonthlyCharges": 80.45,
                            "TotalCharges": 90.23
                        })
    assert r.status_code == 403

# ----- Valid prediction ------
def test_predict_valid():
    r = requests.post(f"{BASE_URL}/predict",
                      headers=HEADERS,
                      json={
                            "Gender": "Female",
                            "SeniorCitizen": 0,
                            "Partner": "Yes",
                            "Dependents": "No",
                            "Tenure": 25,
                            "PhoneService": "Yes",
                            "MultipleLines": "Yes",
                            "InternetService": "Yes",
                            "OnlineSecurity": "Yes",
                            "OnlineBackup": "No",
                            "DeviceProtection": "No",
                            "TechSupport": "No",
                            "StreamingTV": "Yes",
                            "StreamingMovies": "Yes",
                            "Contract": "1-year",
                            "PaperlessBilling": "Yes",
                            "PaymentMethod": "Bank transfer",
                            "MonthlyCharges": 80.45,
                            "TotalCharges": 90.23
                        })
    assert r.status_code == 200
    data = r.json()
    assert "prediction" in data
    
# ---- Invalid input -----

def test_predict_missing_field():
    r = requests.post(f"{BASE_URL}/predict", headers=HEADERS, json = {"Gender": "Male"})
    assert r.status_code == 422

def test_predict_wrong_type():
    r = requests.post(f"{BASE_URL}/predict",
                      headers=HEADERS,
                      json={
                            "Gender": "Male",
                            "SeniorCitizen": 0,
                            "Partner": "Yes",
                            "Dependents": "3",
                            "Tenure": 25,
                            "PhoneService": "Yes",
                            "MultipleLines": "Yes",
                            "InternetService": "Yes",
                            "OnlineSecurity": "Yes",
                            "OnlineBackup": "No",
                            "DeviceProtection": "No",
                            "TechSupport": "No",
                            "StreamingTV": "Yes",
                            "StreamingMovies": "Yes",
                            "Contract": "1-year",
                            "PaperlessBilling": "Yes",
                            "PaymentMethod": "Bank transfer",
                            "MonthlyCharges": "wrong input",        # Wrong Input
                            "TotalCharges": 90.23
                        })
    assert r.status_code == 422



# ---- Response headers ----
def test_response_time_header():
    r = requests.get(f"{BASE_URL}/health")
    assert "x-process-time-ms" in r.headers