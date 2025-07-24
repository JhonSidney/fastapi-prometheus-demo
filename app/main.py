from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import time
import random

app = FastAPI()

# Cria o instrumentador
instrumentator = Instrumentator().instrument(app).expose(app)

@app.get("/ping")
def ping():
    # (Opcional) simula alguma latência
    time.sleep(random.uniform(0.1, 0.5))
    return {"message": "pong"}
