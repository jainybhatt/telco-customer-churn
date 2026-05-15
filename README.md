# Telco Customer Churn

Focused customer retention programs


## About Dataset

### Context

"Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]

### Content
Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

### The data set includes information about:

Customers who left within the last month – the column is called Churn
Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
Demographic info about customers – gender, age range, and if they have partners and dependents

## Project Overview

This project demonstrates an end-to-end ML pipeline:

- Data preprocessing (encoding + scaling)
- Model training (Logistic Regression)
- Model serialization (joblib)
- REST API deployment (FastAPI)
- Input validation (Pydantic)
- Containerization (Docker + Docker Compose)
- Unit testing (pytest)

---

## Project Structure

telco-customer-churn/
│
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── model_loader.py # Load trained model pipeline
│ ├── schemas/
│ │     └── prediction.py 
│
├── models/
│ └── log_reg_model.pkl # Trained pipeline (scaler + encoder + model)
│
├── notebook/
│ └── Telco_Customer_Churn.ipynb # Model training script
│
├── tests/
│ ├── verify_model.py # verify saved model
│ └── test_api.py # API unit tests
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md


---

## Machine Learning Pipeline

The model pipeline includes:

- OneHotEncoder → categorical variables
- StandardScaler → numerical variables
- Logistic Regression classifier

All steps are wrapped into a single sklearn/imblearn pipeline and saved as:

```bash
models/log_reg_model.pkl

--

## Tech Stack
Python 3.11
FastAPI
Scikit-learn
Pandas
NumPy
Imbalanced-learn
Joblib
Pydantic
Uvicorn
Docker

--

## Installation (Local Setup)
    1. Clone repository
        git clone https://github.com/your-username/telco-customer-churn.git
        cd telco-customer-churn

    2. Create virtual environment
        python -m venv venv
        source venv/bin/activate   # Mac/Linux
        venv\Scripts\activate      # Windows

    3. Install dependencies
        pip install -r requirements.txt
        Run the API
        Start FastAPI server
        uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
        Open API Docs
    Swagger UI: http://127.0.0.1:8000/docs
    
    ### API Endpoints
    
    - Health Check
        GET /

        Response:

        {
        "message": "Telco Churn API is running"
        }
    
    
    - Prediction Endpoint
        POST /predict
        Example Request
        {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.5,
        "TotalCharges": 840.6
        }

        Example Response
        {
        "churn_prediction": "Yes",
        "churn_probability": 0.59
        }


Invalid input returns:

422 Unprocessable Entity

## Run with Docker
    Build and start containers
    docker compose up --build -d
    Stop containers
    docker compose down

## Run Tests
pytest tests/

## Common Issues
1. Model loading error

    Ensure same library versions used for training and inference.

2. NumPy / Pandas compatibility error

    Use stable versions:

    numpy==1.26.4
    pandas==2.2.3
    
3. imblearn missing
    pip install imbalanced-learn

4. Docker daemon error

Ensure Docker Desktop is running:

Docker Desktop (Container platform)

## Key Learnings
End-to-end ML deployment workflow
Data preprocessing pipelines
Model serialization pitfalls
API design with FastAPI
Input/output validation with Pydantic
Docker containerization
Debugging dependency mismatches

## Future Improvements
Add MLflow model tracking
Add monitoring (drift detection)
Replace Logistic Regression with XGBoost
Deploy on AWS / GCP
CI/CD pipeline (GitHub Actions)

### Author 

Jainy Bhatt
