from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from src.app.models.common import VehicleType, VehicleCondition, VehicleStatus


class Vehicle(SQLModel, table=True):
    # __tablename__ defaults to "vehicle" (class name lowercased)

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    vehicle_type: VehicleType
    title: str = Field(max_length=150, index=True)
    description: Optional[str] = None

    make: Optional[str] = Field(default=None, max_length=50, index=True)
    model: Optional[str] = Field(default=None, max_length=50, index=True)
    trim: Optional[str] = Field(default=None, max_length=50)
    year_of_manufacture: Optional[int] = None

    condition: VehicleCondition = VehicleCondition.USED
    status: VehicleStatus = VehicleStatus.DRAFT

    district: Optional[str] = Field(default=None, index=True)
    city: Optional[str] = None

    is_featured: bool = False
    is_verified: bool = False

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)},
    )

    # ---- one-to-one relations (uselist=False) ----
    specs: Optional["VehicleSpecs"] = Relationship(
        back_populates="vehicle",
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"},
    )
    pricing: Optional["VehiclePricing"] = Relationship(
        back_populates="vehicle",
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"},
    )
    documents: Optional["VehicleDocuments"] = Relationship(
        back_populates="vehicle",
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"},
    )
    history: Optional["VehicleHistory"] = Relationship(
        back_populates="vehicle",
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"},
    )

    # ---- one-to-many relation ----
    media: list["VehicleMedia"] = Relationship(
        back_populates="vehicle",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )


# Imported at the bottom so the forward-referenced relationship types resolve.
from src.app.models.vehicle.vehicleSpecs import VehicleSpecs        # noqa: E402
from src.app.models.vehicle.vehiclePricing import VehiclePricing    # noqa: E402
from src.app.models.vehicle.vehicleDocuments import VehicleDocuments  # noqa: E402
from src.app.models.vehicle.vehicleHistory import VehicleHistory    # noqa: E402
from src.app.models.vehicle.vehicleMedia import VehicleMedia        # noqa: E402
