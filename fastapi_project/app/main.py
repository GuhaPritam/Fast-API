from fastapi import FastAPI
from app.api.v1.router_v1 import router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1", tags=["v1"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Project!"}

