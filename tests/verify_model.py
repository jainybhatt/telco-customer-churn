import joblib
import numpy as np

# Load the model
model = joblib.load("models/log_reg_model.pkl")
print(f"Model type: {type(model)}")
print(f"Model loaded successfully.")

# Check if it's a pipeline

if hasattr(model, "steps"):
    print(f"Pipeline steps: {[step[0] for step in model.steps]}")

# Make the prediction with a dummy data

test_input = np.array([[0,0,1,1,12,0,0,1,1,1,1,1,0,0,1,0,1,50.6,76.1]])
prediction = model.predict(test_input)
print(f"Test prediction: {prediction}")

if hasattr(model, "predict_proba"):
    probabilities = model.predict_proba(test_input)
    print(f"Probabilities: {probabilities}")