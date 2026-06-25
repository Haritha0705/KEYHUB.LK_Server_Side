from typing import TYPE_CHECKING
from sqlalchemy import Enum, String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.common import MediaType
from src.app.models.vehicle.base import VehicleSubBase
if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleMedia(VehicleSubBase, table=True):

    __tablename__ = "vehicle_media"

    url: Mapped[str] = mapped_column(String(500), nullable=False)
    media_type: Mapped[MediaType] = mapped_column(Enum(MediaType, name="media_type"), default=MediaType.IMAGE)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)
    position: Mapped[int] = mapped_column(Integer, default=0)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: Mapped[Vehicle] = relationship(back_populates="media")