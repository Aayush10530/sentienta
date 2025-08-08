from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from .model import DummyModel

app = FastAPI(title="Dummy ML Model API", version="0.1.0")
MODEL = DummyModel(version="v1.0-demo")

class PredictRequest(BaseModel):
    data: Dict[str, Any]

class PredictResponse(BaseModel):
    model_version: str
    input_summary: Dict[str, Any]
    prediction: Dict[str, Any]

@app.get("/")
def root():
    return {"message": "Dummy ML Model API. POST /predict with JSON {\"data\": {...}}"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if not isinstance(req.data, dict):
        raise HTTPException(status_code=400, detail="data must be an object")
    return MODEL.predict(req.data)

