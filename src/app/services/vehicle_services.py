from sqlmodel import Session

from src.app.mapper.vehicle_mapper import VehicleMapper
from src.app.repository.vehicle_repository import VehicleRepository
from src.app.schemas.vehicle.vehicle import VehicleRequest, VehicleResponse

class VehicleService:

    def __init__(self, session: Session):
        self.repo = VehicleRepository(session)

    def create_vehicle(self, data: VehicleRequest) -> VehicleResponse:
        vehicle_model = VehicleMapper.to_model(data)

        saved_vehicle = self.repo.create(vehicle_model)

        return VehicleMapper.to_response(saved_vehicle)