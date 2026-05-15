from pydantic import BaseModel, Field

class ChurnInput(BaseModel):
    Gender: object = Field(..., description="Gender of the customer", example = 'Male'), 
    SeniorCitizen: float = Field(..., description="Is customer a senior citizen", example = 0), 
    Partner: object = Field(..., description="Does customer have partner", example = 'Yes'),
    Dependents: object = Field(..., description="Does customer have dependents", example = 'Yes'),
    Tenure: float = Field(..., description="Months as customer", example = 0),
    PhoneService: object = Field(..., description="Does customer have phone service", example = 'Yes'), 
    MultipleLines: object = Field(..., description="Does customer have multiple lines", example = 'Yes'), 
    InternetService: object = Field(..., description="Does customer have internet service", example = 'Yes'),
    OnlineSecurity: object = Field(..., description="Does customer have online security", example = 'Yes'), 
    OnlineBackup: object = Field(..., description="Does customer have online backup", example = 'Yes'),
    DeviceProtection: object = Field(..., description="Does customer have device protection", example = 'Yes'), 
    TechSupport: object = Field(..., description="Does customer have tech support", example = 'Yes'), 
    StreamingTV: object = Field(..., description="Does customer have streaming tv service", example ='Yes'), 
    StreamingMovies: object = Field(..., description="Does customer have streaming movies service", example ='Yes'), 
    Contract: object = Field(..., description="how long is the contract", example = 'One year'), 
    PaperlessBilling: object = Field(..., description="Does customer have paperless billing", example = 'Yes'), 
    PaymentMethod: object = Field(..., description="which payment method is used by customer",example = 'Electronic check'), 
    MonthlyCharges: float = Field(..., description="what is the monthly charges", example = 20.0), 
    TotalCharges: float = Field(..., description="What is total charge amount", example = 20.0)


class ChurnOutput(BaseModel):
      prediction: str
      #prediction_label: str
      probability: float
      #probabilities: dict[str, float]
      