from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Numeric, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.models.vehicle.base import VehicleSubBase
if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehiclePricing(VehicleSubBase, table=True):

    __tablename__ = "vehicle_pricing"

    price: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False, index=True)
    currency: Mapped[str] = mapped_column(String(3), default="LKR")
    negotiable: Mapped[bool] = mapped_column(Boolean, default=False)
    leasing_available: Mapped[bool] = mapped_column(Boolean, default=False)
    monthly_payment: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: Mapped[Vehicle] = relationship(back_populates="pricing")