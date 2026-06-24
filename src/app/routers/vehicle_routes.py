from fastapi import APIRouter

from src.app.core.db import SessionDep
from src.app.schemas.vehicle.vehicle import VehicleResponse, VehicleRequest
from src.app.services.vehicle_services import VehicleService

vehicle_router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@vehicle_router.post("/", response_model=VehicleResponse, status_code=201)
def create_vehicle(
        payload: VehicleRequest,
        session: SessionDep,
):
    service = VehicleService(session)
    return service.create_vehicle(payload)