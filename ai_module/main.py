from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np

app = FastAPI()

model = load("decision_tree_model.joblib")
scaler = load("scaler.joblib")

class FaultInput(BaseModel):
    Va: float
    Vb: float
    Vc: float
    Ia: float
    Ib: float
    Ic: float

@app.post("/predict")
def predict(data: FaultInput):
    features = np.array([[ 
        data.Va,
        data.Vb,
        data.Vc,
        data.Ia,
        data.Ib,
        data.Ic
    ]])

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    return {
        "G": int(prediction[0]),
        "A": int(prediction[1]),
        "B": int(prediction[2]),
        "C": int(prediction[3])
    }
