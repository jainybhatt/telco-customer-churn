from fastapi import FastAPI
import joblib

# Load model at startup
model = joblib.load("models/log_reg_model.pkl")

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