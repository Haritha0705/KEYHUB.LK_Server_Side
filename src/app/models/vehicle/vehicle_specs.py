from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import Integer, Enum, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.common import FuelType, Transmission
from src.app.models.vehicle.base import VehicleSubBase
if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleSpecs(VehicleSubBase):

    __tablename__ = "vehicle_specs"

    mileage: Mapped[int | None] = mapped_column(Integer, index=True)
    engine_capacity_cc: Mapped[int | None] = mapped_column(Integer, index=True)
    fuel_type: Mapped[FuelType | None] = mapped_column(Enum(FuelType, name="fuel_type"), index=True)
    transmission: Mapped[Transmission | None] = mapped_column(Enum(Transmission, name="transmission"), index=True)
    body_type: Mapped[str | None] = mapped_column(String(40), index=True)
    color: Mapped[str | None] = mapped_column(String(30))
    seating_capacity: Mapped[int | None] = mapped_column(Integer)
    doors: Mapped[int | None] = mapped_column(Integer)
    drivetrain: Mapped[str | None] = mapped_column(String(20))  # FWD / RWD / AWD / 4WD

    # Anything specific to a vehicle type lives here. Flexible, no migrations.
    extra_specs: Mapped[dict | None] = mapped_column(JSONB, default=dict)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: Mapped[Vehicle] = relationship(back_populates="specs")