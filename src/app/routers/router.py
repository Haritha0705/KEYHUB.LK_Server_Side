from fastapi import APIRouter

from src.app.routers.vehicle_routes import vehicle_router

api_v1_router = APIRouter(prefix="/api/v1")

# Vehicle Router
api_v1_router.include_router(vehicle_router)