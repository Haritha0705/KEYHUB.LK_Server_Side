from __future__ import annotations

import uuid
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class VehiclePricing(SQLModel, table=True):
    # __tablename__ = "vehiclepricing"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    vehicle_id: uuid.UUID = Field(foreign_key="vehicle.id", nullable=False, unique=True)

    # TODO: match VehiclePricingRequest, e.g.:
    # price: Optional[float] = None
    # currency: str = "LKR"
    # is_negotiable: bool = False

    vehicle: Optional["Vehicle"] = Relationship(back_populates="pricing")
