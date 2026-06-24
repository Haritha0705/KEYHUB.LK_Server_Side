from typing import TYPE_CHECKING
from sqlmodel import Field, String, Enum, Column, Relationship

from src.app.models.common import MediaType
from src.app.models.vehicle.base import VehicleSubBase

if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleMedia(VehicleSubBase, table=True):

    __tablename__ = "vehicle_media"

    url: str = Field(sa_type=String(500))

    media_type: MediaType = Field(sa_column=Column(Enum(MediaType, name="media_type"), default=MediaType.IMAGE))

    is_primary: bool = Field(default=False)

    position: int = Field(default=0)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: "Vehicle" = Relationship(back_populates="media")