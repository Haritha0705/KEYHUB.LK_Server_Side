from decimal import Decimal
from pydantic import BaseModel, Field

from src.app.models.common import VehicleType, VehicleCondition, FuelType, Transmission

class VehicleFilter(BaseModel):
    # basic filters
    vehicle_type: VehicleType | None = None
    make: str | None = None
    model: str | None = None
    condition: VehicleCondition | None = None

    # price range
    min_price: Decimal | None = Field(default=None, ge=0)
    max_price: Decimal | None = Field(default=None, ge=0)

    # specs filters
    fuel_type: FuelType | None = None
    transmission: Transmission | None = None
    min_year: int | None = Field(default=None, ge=1900, le=2100)
    max_year: int | None = Field(default=None, ge=1900, le=2100)
    min_mileage: int | None = Field(default=None, ge=0)
    max_mileage: int | None = Field(default=None, ge=0)

    # location
    district: str | None = None
    city: str | None = None

    # flags
    is_featured: bool | None = None
