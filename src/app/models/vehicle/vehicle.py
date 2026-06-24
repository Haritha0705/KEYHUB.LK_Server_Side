import uuid
from sqlmodel import Field, Column, Enum, String, Text, ForeignKey, Relationship
from typing import Optional, List

from src.app.models.vehicle.vehicleDocuments import VehicleDocuments
from src.app.models.vehicle.vehicleHistory import VehicleHistory
from src.app.models.vehicle.vehicleMedia import VehicleMedia
from src.app.models.vehicle.vehiclePricing import VehiclePricing
from src.app.models.vehicle.vehicleSpecs import VehicleSpecs
from src.app.models.common import BaseModel, VehicleType, VehicleCondition, VehicleStatus

class Vehicle(BaseModel, table=True):

    __tablename__ = "vehicle"

    vehicle_type: VehicleType = Field(sa_column=Column(Enum(VehicleType, name="vehicle_type"), index=True))

    title: str = Field(sa_type=String(150))

    description: str | None = Field(default=None, sa_type=Text, nullable=True)

    make: str | None = Field(default=None, sa_type=String(50), nullable=True, index=True)

    model: str | None = Field(default=None, sa_type=String(50), nullable=True, index=True)

    trim: str | None = Field(default=None, sa_type=String(50), nullable=True)

    year_of_manufacture: int | None = Field(default=None, nullable=True, index=True)

    condition: VehicleCondition = Field(sa_column=Column(Enum(VehicleCondition, name="vehicle_condition"), default=VehicleCondition.USED))

    status: VehicleStatus = Field(sa_column=Column(Enum(VehicleStatus, name="vehicle_status"),default=VehicleStatus.DRAFT,index=True))

    district: str | None = Field(default=None, sa_type=String(50), nullable=True, index=True)

    city: str | None = Field(default=None, sa_type=String(50), nullable=True, index=True)

    is_featured: bool = Field(default=False)

    is_verified: bool = Field(default=False)

    # ONE-TO-ONE RELATIONSHIPS

    specs: Optional["VehicleSpecs"] = Relationship(back_populates="vehicle")

    documents: Optional["VehicleDocuments"] = Relationship(back_populates="vehicle")

    pricing: Optional["VehiclePricing"] = Relationship(back_populates="vehicle")

    history: Optional["VehicleHistory"] = Relationship(back_populates="vehicle")

    # ONE-TO-MANY RELATIONSHIP

    media: List["VehicleMedia"] = Relationship(back_populates="vehicle", sa_relationship_kwargs={"order_by": "VehicleMedia.position"})

    # Index

