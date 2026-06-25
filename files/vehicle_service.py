import logging
import uuid

from sqlmodel import Session
from sqlalchemy.exc import IntegrityError

from app.core.errors import APIError
from src.app.mapper.vehicle_mapper import VehicleMapper
from src.app.repository.vehicle_repository import VehicleRepository
from src.app.services.vehicle_audit_service import VehicleAuditService
from src.app.schemas.vehicle.vehicle import VehicleRequest, VehicleResponse

logger = logging.getLogger(__name__)


class VehicleService:
    """Orchestrates the create-vehicle business operation.

    Owns the transaction boundary: the repository and audit service only stage
    rows; this service decides when to commit and rolls back on any failure so
    the vehicle and its audit record always succeed or fail together.
    """

    def __init__(self, session: Session):
        self.session = session
        self.repo = VehicleRepository(session)
        self.audit = VehicleAuditService(session)

    def create_vehicle(self, data: VehicleRequest, user_id: uuid.UUID) -> VehicleResponse:
        try:
            vehicle_model = VehicleMapper.to_model(data)

            # 1. stage + flush (id is populated, but not committed yet)
            saved_vehicle = self.repo.add(vehicle_model)

            # 2. audit trail in the SAME transaction
            self.audit.record_create(vehicle=saved_vehicle, user_id=user_id)

            # 3. one commit for the whole operation
            self.session.commit()
            self.session.refresh(saved_vehicle)

            logger.info("Vehicle created id=%s by user=%s", saved_vehicle.id, user_id)
            return VehicleMapper.to_response(saved_vehicle)

        except APIError:
            # already a well-formed error - roll back and re-raise untouched
            self.session.rollback()
            raise

        except IntegrityError as e:
            # duplicate key, bad FK, NOT NULL violation, etc. -> client error 409
            self.session.rollback()
            logger.warning("Integrity error creating vehicle: %s", e)
            raise APIError(
                code=409,
                message="Vehicle violates a uniqueness or foreign-key constraint",
            )

        except Exception as e:
            self.session.rollback()
            # logger.exception() captures the full traceback in your logs,
            # while the client only sees a clean message.
            logger.exception("Unexpected error creating vehicle")
            raise APIError(
                code=400,
                message=f"Error adding vehicle: {e.__class__.__name__}: {e}",
            )
