from pydantic import Field

from src.app.models.common import FuelType, Transmission
from src.app.schemas.base import Base, IDMixin

class VehicleSpecsBase(Base):
    fuel_type: FuelType | None = None
    transmission: Transmission | None = None
    body_type: str | None = None
    color: str | None = None
    drivetrain: str | None = None

class VehicleSpecsRequest(VehicleSpecsBase):
    mileage: int | None = Field(default=None, ge=0)
    engine_capacity_cc: int | None = Field(default=None, ge=0)
    seating_capacity: int | None = Field(default=None, ge=0)
    doors: int | None = Field(default=None, ge=0)
    extra_specs: dict | None = Field(default_factory=dict)

class VehicleSpecsResponse(IDMixin, VehicleSpecsBase):
    mileage: int | None = None
    engine_capacity_cc: int | None = None
    seating_capacity: int | None = None
    doors: int | None = None
    extra_specs: dict | None = None