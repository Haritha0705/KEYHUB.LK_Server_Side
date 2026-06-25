from sqlalchemy.orm import Session

from src.app.models.vehicle.vehicle import Vehicle


class VehicleRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(self, vehicle: Vehicle) -> Vehicle:
        self.session.add(vehicle)
        self.session.flush()
        return vehicle
