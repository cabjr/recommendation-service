from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from .vw_model import train_example, predict_example
from .logger import logger
from .database import engine, metadata
from sqlalchemy import Table, Column, Integer, String, Float, JSON, insert
from .models import Item

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.error(f"Error occurred: {exc}")
    return {"error": str(exc)}

# Define SQLAlchemy table to represent our items
items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("features", JSON),
    Column("label", Float),
    Column("prediction", Float),
)

@app.post("/train")
async def train(item: Item):
    try:
        train_example(item)
        # persist event
        with engine.connect() as connection:
            result = connection.execute(
                insert(items).values(features=item.features, label=item.label)
            )
        logger.info(f"Training successful for item with id {result.inserted_primary_key}")
        return {"detail": "Training successful"}
    except Exception as e:
        logger.error(f"Error during training: {e}")
        raise HTTPException(status_code=500, detail="Training error")

@app.post("/predict")
async def predict(item: Item):
    try:
        prediction = predict_example(item)
        # persist event
        with engine.connect() as connection:
            result = connection.execute(
                insert(items).values(features=item.features, prediction=prediction)
            )
        logger.info(f"Prediction successful for item with id {result.inserted_primary_key}")
        return {"prediction": prediction}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Prediction error")
