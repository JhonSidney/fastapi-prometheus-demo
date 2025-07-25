from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import time
import random

app = FastAPI()

instrumentator = Instrumentator()

# Instrumenta a app e expõe as métricas ANTES do app iniciar
instrumentator.instrument(app).expose(app)

@app.get("/ping")
def ping():
    time.sleep(random.uniform(0.1, 0.5))
    return {"message": "pong"}

@app.get("/slow")
def slow():
    time.sleep(random.uniform(0.1, 1.5))
    return {"message": "slow response"}
