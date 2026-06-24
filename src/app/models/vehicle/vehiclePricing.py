from decimal import Decimal
from typing import TYPE_CHECKING
from sqlmodel import Field, Numeric, Relationship

from src.app.models.vehicle.base import VehicleSubBase

if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehiclePricing(VehicleSubBase, table=True):

    __tablename__ = "vehicle_pricing"

    price: Decimal = Field(sa_type=Numeric(14, 2), index=True)

    currency: str = Field(max_length=5, default="LKR")

    negotiable: bool = Field(default=False)

    leasing_available: bool = Field(default=False)

    monthly_payment: Decimal | None = Field(default=None, sa_type=Numeric(14, 2), nullable=True)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: "Vehicle" = Relationship(back_populates="pricing")