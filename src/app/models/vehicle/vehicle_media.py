from __future__ import annotations

import uuid
from typing import TYPE_CHECKING
from sqlalchemy import Enum, String, Boolean, Integer, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.common import BaseModel, MediaType
if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleMedia(BaseModel):

    __tablename__ = "vehicle_media"

    vehicle_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("vehicles.id", ondelete="CASCADE"), index=True, nullable=False)

    url: Mapped[str] = mapped_column(String(500), nullable=False)
    media_type: Mapped[MediaType] = mapped_column(Enum(MediaType, name="media_type"), default=MediaType.IMAGE)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)
    position: Mapped[int] = mapped_column(Integer, default=0)

    # MANY-TO-ONE RELATIONSHIP

    vehicle: Mapped[Vehicle] = relationship(back_populates="media")
