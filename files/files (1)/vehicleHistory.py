from __future__ import annotations

import uuid
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class VehicleHistory(SQLModel, table=True):
    # __tablename__ = "vehiclehistory"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    vehicle_id: uuid.UUID = Field(foreign_key="vehicle.id", nullable=False, unique=True)

    # TODO: match VehicleHistoryRequest, e.g.:
    # number_of_previous_owners: Optional[int] = None
    # accident_history: Optional[str] = None
    # service_record_available: bool = False

    vehicle: Optional["Vehicle"] = Relationship(back_populates="history")
