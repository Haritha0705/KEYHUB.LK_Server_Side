from typing import TYPE_CHECKING
from sqlmodel import Field, Text, Relationship

from src.app.models.vehicle.base import VehicleSubBase

if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleHistory(VehicleSubBase, table=True):

    __tablename__ = "vehicle_history"

    previous_owners: int = Field(default=0)

    had_accidents: bool = Field(default=False)

    accident_history: str | None = Field(default=None, sa_type=Text, nullable=True)

    service_history: str | None = Field(default=None, sa_type=Text, nullable=True)

    import_details: str | None = Field(default=None, sa_type=Text, nullable=True)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: "Vehicle" = Relationship(back_populates="history")
