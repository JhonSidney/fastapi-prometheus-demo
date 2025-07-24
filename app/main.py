from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import time
import random

app = FastAPI()

instrumentator = Instrumentator()

@app.get("/ping")
def ping():
    return {"message": "pong"}