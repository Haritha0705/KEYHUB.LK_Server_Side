import logging

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.core.errors import APIError
from src.app.mapper.vehicle_mapper import VehicleMapper
from src.app.repository.vehicle_repository import VehicleRepository
from src.app.schemas.vehicle.vehicle import VehicleRequest, VehicleResponse

logger = logging.getLogger(__name__)

class VehicleService:

    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = VehicleRepository(session)

    async def create_vehicle(self, data: VehicleRequest) -> VehicleResponse:
        try:
            vehicle = VehicleMapper.to_model(data)
            saved = await self.repo.create(vehicle)

            await self.session.commit()

            loaded = await self.repo.get_by_id(saved.id)

            if loaded is None:
                raise APIError(code=404, message="Vehicle not found after creation")

            logger.info("Vehicle created id=%s", saved.id)
            return VehicleMapper.to_response(loaded)

        except APIError:
            await self.session.rollback()
            raise

        except IntegrityError as e:
            await self.session.rollback()
            logger.warning("Integrity error creating vehicle: %s", e)
            raise APIError(
                code=409,
                message="Vehicle violates a uniqueness or foreign-key constraint",
            )

        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.exception("Database error creating vehicle")
            raise APIError(code=400, message=f"Error adding vehicle: {e.__class__.__name__}")

        except Exception:
            await self.session.rollback()
            logger.exception("Unexpected error creating vehicle")
            raise APIError(code=500, message="Internal server error")
