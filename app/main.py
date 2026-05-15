from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from app.schemas.prediction import ChurnInput, ChurnOutput


# Load model at startup
model = joblib.load('models/log_reg_model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')

# Label mapping (for classification — adjust for your project)
LABEL_MAP = {0: "No Churn", 1: "Churn"}

app = FastAPI(
    title="Logistic Regression model API.",
    description="Production-style log reg serving API.",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
        }

@app.post("/predict", response_model=ChurnOutput)
def predict(data: ChurnInput):
    features = np.array([[
        data.Gender,
        data.SeniorCitizen, 
        data.Partner, 
        data.Dependents, 
        data.Tenure, 
        data.PhoneService, 
        data.MultipleLines, 
        data.InternetService, 
        data.OnlineSecurity, 
        data.OnlineBackup, 
        data.DeviceProtection, 
        data.TechSupport, 
        data.StreamingTV, 
        data.StreamingMovies, 
        data.Contract, 
        data.PaperlessBilling, 
        data.PaymentMethod, 
        data.MonthlyCharges, 
        data.TotalCharges
    ]])


    # Convert request to dataframe
    features_df = pd.DataFrame(
        [data.model_dump()]
    )

    # Prediction
    prediction = model.predict(features_df)[0]

    probability = model.predict_proba(features_df)[0][1]

    return {
        "prediction": (
            "Yes" if prediction == 1 else "No"
        ),
        "probability": round(
            float(probability),
            4
        )
    }