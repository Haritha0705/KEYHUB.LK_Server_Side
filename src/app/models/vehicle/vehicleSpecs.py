from typing import TYPE_CHECKING
from sqlmodel import Field, Enum, String, JSON, Relationship

from src.app.models.common import FuelType, Transmission
from src.app.models.vehicle.base import VehicleSubBase

if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleSpecs(VehicleSubBase, table=True):

    __tablename__ = "vehicle_specs"

    mileage: int | None = Field(default=None, index=True, nullable=True)

    engine_capacity_cc: int | None = Field(default=None, index=True, nullable=True)

    fuel_type: FuelType | None = Field(default=None, sa_type=Enum(FuelType, name="fuel_type"), index=True, nullable=True)

    transmission: Transmission | None = Field(default=None, sa_type=Enum(Transmission, name="transmission"), index=True, nullable=True)

    body_type: str | None = Field(default=None, sa_type=String(40), index=True, nullable=True)

    color: str | None = Field(default=None, sa_type=String(30), nullable=True)

    seating_capacity: int | None = Field(default=None, nullable=True)

    doors: int | None = Field(default=None, nullable=True)

    drivetrain: str | None = Field(default=None, sa_type=String(20), nullable=True)

    extra_specs: dict | None = Field(default=None, sa_type=JSON, nullable=True)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: "Vehicle" = Relationship(back_populates="specs")