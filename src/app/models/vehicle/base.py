import uuid
from sqlalchemy import ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.app.models.common import BaseModel

class VehicleSubBase(BaseModel):

    __abstract__ = True

    vehicle_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey("vehicles.id", ondelete="CASCADE"),unique=True,nullable=False)
