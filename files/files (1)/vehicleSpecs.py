from __future__ import annotations

import uuid
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class VehicleSpecs(SQLModel, table=True):
    # __tablename__ = "vehiclespecs"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # unique=True enforces the one-to-one (one specs row per vehicle)
    vehicle_id: uuid.UUID = Field(foreign_key="vehicle.id", nullable=False, unique=True)

    # TODO: add the exact columns that exist in VehicleSpecsRequest, e.g.:
    # fuel_type: Optional[str] = None
    # transmission: Optional[str] = None
    # engine_capacity_cc: Optional[int] = None
    # mileage_km: Optional[int] = None

    vehicle: Optional["Vehicle"] = Relationship(back_populates="specs")
