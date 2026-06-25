import logging

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.errors import APIError
from src.app.mapper.vehicle_mapper import VehicleMapper
from src.app.repository.vehicle_repository import VehicleRepository
from src.app.schemas.vehicle.vehicle import VehicleRequest, VehicleResponse

logger = logging.getLogger(__name__)

class VehicleService:

    def __init__(self, session: Session):
        self.session = session
        self.repo = VehicleRepository(session)

    def create_vehicle(self, data: VehicleRequest) -> VehicleResponse:
        try:
            vehicle = VehicleMapper.to_model(data)
            saved = self.repo.create(vehicle)

            self.session.commit()
            self.session.refresh(saved)

            logger.info("Vehicle created id=%s", saved.id)
            return VehicleMapper.to_response(saved)

        except APIError:
            self.session.rollback()
            raise

        except IntegrityError as e:
            self.session.rollback()
            logger.warning("Integrity error creating vehicle: %s", e)
            raise APIError(
                code=409,
                message="Vehicle violates a uniqueness or foreign-key constraint",
            )

        except SQLAlchemyError as e:
            self.session.rollback()
            logger.exception("Database error creating vehicle")
            raise APIError(code=400, message=f"Error adding vehicle: {e.__class__.__name__}")

        except Exception:
            self.session.rollback()
            logger.exception("Unexpected error creating vehicle")
            raise APIError(code=500, message="Internal server error")
