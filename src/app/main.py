from fastapi import FastAPI

from src.app.core.errors import register_exception_handlers
from src.app.routers.router import api_v1_router

app = FastAPI()

register_exception_handlers(app)

@app.get("/")
def read_root():
    return {"Status": "ok"}


app.include_router(api_v1_router)
