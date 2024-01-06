from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/{str}")
def predict_hate_speech(string: str):
    return {'prediction_result': "no_hate_speech"}
