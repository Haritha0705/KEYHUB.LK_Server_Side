from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.app.core.db import SessionDep
from src.app.schemas.vehicle.vehicle import VehicleRequest, VehicleResponse
from src.app.services.vehicle_services import VehicleService

vehicle_router = APIRouter(prefix="/vehicles", tags=["vehicles"])

def get_vehicle_service(session: SessionDep) -> VehicleService:
    return VehicleService(session)

ServiceDep = Annotated[VehicleService, Depends(get_vehicle_service)]

@vehicle_router.post(
    "/",
    response_model=VehicleResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Invalid input"},
        409: {"description": "Conflicting / duplicate vehicle"},
    },
    summary="Create a vehicle",
)
async def create_vehicle(
    payload: VehicleRequest,
    service: ServiceDep,
) -> VehicleResponse:
    return await service.create_vehicle(payload)
