from fastapi import FastAPI

from src.app.routers.router import api_v1_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "ok"}

app.include_router(api_v1_router)
