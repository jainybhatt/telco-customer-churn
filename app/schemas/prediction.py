from pydantic import BaseModel, Field

class ChurnInput(BaseModel):
    Gender: object = Field(..., pattern = "^(Female|Male)$",description="Gender of the customer", example = 'Male'), 
    SeniorCitizen: float = Field(..., description="Is customer a senior citizen", example = 0), 
    Partner: object = Field(..., pattern = "^(Yes|No)$",description="Does customer have partner", example = 'Yes'),
    Dependents: object = Field(..., pattern = "^(Yes|No)$", description="Does customer have dependents", example = 'Yes'),
    Tenure: float = Field(..., description="Months as customer", example = 0),
    PhoneService: object = Field(..., pattern = "^(Yes|No)$",description="Does customer have phone service", example = 'Yes'), 
    MultipleLines: object = Field(..., pattern = "^(No phone service|Yes|No)$",description="Does customer have multiple lines", example = 'Yes'), 
    InternetService: object = Field(..., pattern = "^(DSL|Fiber optic|No)$" ,description="Does customer have internet service", example = 'Yes'),
    OnlineSecurity: object = Field(..., pattern = "^(No internet service|Yes|No)$",description="Does customer have online security", example = 'Yes'), 
    OnlineBackup: object = Field(..., pattern = "^(No internet service|Yes|No)$", description="Does customer have online backup", example = 'Yes'),
    DeviceProtection: object = Field(..., pattern = "^(No internet service|Yes|No)$", description="Does customer have device protection", example = 'Yes'), 
    TechSupport: object = Field(..., pattern = "^(No internet service|Yes|No)$", description="Does customer have tech support", example = 'Yes'), 
    StreamingTV: object = Field(..., pattern = "^(No internet service|Yes|No)$", description="Does customer have streaming tv service", example ='Yes'), 
    StreamingMovies: object = Field(..., pattern = "^(No internet service|Yes|No)$", description="Does customer have streaming movies service", example ='Yes'), 
    Contract: object = Field(..., pattern="^(Month-to-month|One year|Two year)$", description="how long is the contract", example = 'One year'), 
    PaperlessBilling: object = Field(..., description="Does customer have paperless billing", example = 'Yes'), 
    PaymentMethod: object = Field(..., pattern="^(Electronic check|Mailed check|Bank transfer| Credit card)$" ,description="which payment method is used by customer",example = 'Electronic check'), 
    MonthlyCharges: float = Field(..., description="what is the monthly charges", example = 20.0), 
    TotalCharges: float = Field(..., description="What is total charge amount", example = 20.0)


class ChurnOutput(BaseModel):
      prediction: str
      #prediction_label: str
      probability: float
      #probabilities: dict[str, float]
      