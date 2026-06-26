import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from src.app.models.vehicle.vehicle import Vehicle

class VehicleRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, vehicle: Vehicle) -> Vehicle:
        self.session.add(vehicle)
        await self.session.flush()
        return vehicle

    async def get_by_id(self, vehicle_id: uuid.UUID) -> Vehicle | None:
        stmt = (
            select(Vehicle)
            .where(Vehicle.id == vehicle_id)
            .options(
                selectinload(Vehicle.specs),
                selectinload(Vehicle.pricing),
                selectinload(Vehicle.documents),
                selectinload(Vehicle.history),
                selectinload(Vehicle.media),
            )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
