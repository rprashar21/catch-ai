from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

# add instrumentation to prometheus
Instrumentator().instrument(app).expose(app)


@app.get("/root")
async def home():
    return {'message':'FastApi with prometheus'}