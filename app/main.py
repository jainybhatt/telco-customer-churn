from fastapi import FastAPI

app = FastAPI(
    title="Logistic Regression model API.",
    description="Production-style log reg serving API.",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "healthy"}