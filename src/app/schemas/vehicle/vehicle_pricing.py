from decimal import Decimal
from pydantic import Field

from src.app.schemas.base import Base, IDMixin

class VehiclePricingRequest(Base):
    price: Decimal = Field(..., gt=0, max_digits=14, decimal_places=2)
    currency: str = Field(default="LKR", min_length=3, max_length=3)
    negotiable: bool = False
    leasing_available: bool = False
    monthly_payment: Decimal | None = Field(default=None, gt=0, max_digits=14, decimal_places=2)

class VehiclePricingResponse(IDMixin, Base):
    price: Decimal
    currency: str
    negotiable: bool
    leasing_available: bool
    monthly_payment: Decimal | None = None