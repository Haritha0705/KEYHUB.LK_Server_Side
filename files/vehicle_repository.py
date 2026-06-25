import logging
import uuid

from sqlmodel import Session

from src.app.models.vehicle.vehicle import Vehicle

logger = logging.getLogger(__name__)


class VehicleRepository:
    """Data-access layer. The ONLY place that touches the DB session for vehicles.

    Important: methods here do NOT commit. They add + flush so DB-generated
    fields (like the id) are populated, but the *service* owns the transaction
    boundary (commit / rollback). This lets the service group several writes
    (e.g. the vehicle + its audit record) into a single atomic operation.
    """

    def __init__(self, session: Session):
        self.session = session

    def add(self, vehicle: Vehicle) -> Vehicle:
        self.session.add(vehicle)
        self.session.flush()      # surfaces integrity errors + populates vehicle.id
        self.session.refresh(vehicle)
        return vehicle

    def get_by_id(self, vehicle_id: uuid.UUID) -> Vehicle | None:
        return self.session.get(Vehicle, vehicle_id)
