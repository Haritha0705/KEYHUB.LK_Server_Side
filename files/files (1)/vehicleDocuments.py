from __future__ import annotations

import uuid
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class VehicleDocuments(SQLModel, table=True):
    # __tablename__ = "vehicledocuments"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    vehicle_id: uuid.UUID = Field(foreign_key="vehicle.id", nullable=False, unique=True)

    # TODO: match VehicleDocumentsRequest, e.g.:
    # registration_number: Optional[str] = None
    # has_valid_revenue_licence: bool = False
    # insurance_provider: Optional[str] = None

    vehicle: Optional["Vehicle"] = Relationship(back_populates="documents")
