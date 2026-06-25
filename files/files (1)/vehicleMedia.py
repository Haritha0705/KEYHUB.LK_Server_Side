from __future__ import annotations

import uuid
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class VehicleMedia(SQLModel, table=True):
    # __tablename__ = "vehiclemedia"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # NOT unique -> one-to-many (a vehicle can have many media rows)
    vehicle_id: uuid.UUID = Field(foreign_key="vehicle.id", nullable=False, index=True)

    # TODO: match VehicleMediaRequest, e.g.:
    # url: str
    # media_type: Optional[str] = None      # image / video
    # is_primary: bool = False
    # sort_order: int = 0

    vehicle: Optional["Vehicle"] = Relationship(back_populates="media")
