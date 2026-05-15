from fastapi import FastAPI, Security, Request
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
import logging
import time
import joblib
import pandas as pd
import numpy as np
from app.schemas.prediction import ChurnInput, ChurnOutput
from app.config import settings

# Auth setup
API_KEY = settings.api_key
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail ="Missing API key")
    if api_key != API_KEY:
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("api")




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

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request logging middleware
@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time) * 1000
    logger.info(f"{request.method} {request.url.path} -> {response.status_code} ({duration_ms:.1f}ms)")
    response.headers["X-Process-Time-Ms"] = f"{duration_ms:.1f}"
    return response


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
        }

@app.post("/predict", response_model=ChurnOutput)
def predict(data: ChurnInput, api_key: str = Security(verify_api_key)):
    
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
