import uuid
from datetime import datetime
from enum import StrEnum
from sqlalchemy import DateTime, func, UUID
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False)

class BaseModel(DeclarativeBase, TimestampMixin):
    __abstract__ = True
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

# SHARED ENUMS

class VehicleType(StrEnum):
    CAR = "CAR"
    SUV = "SUV"
    JEEP = "JEEP"
    VAN = "VAN"
    MOTORBIKE = "MOTORBIKE"
    SCOOTER = "SCOOTER"
    THREE_WHEELER = "THREE_WHEELER"
    PICKUP = "PICKUP"
    LORRY = "LORRY"
    TRUCK = "TRUCK"
    BUS = "BUS"
    TRACTOR = "TRACTOR"
    HEAVY_MACHINERY = "HEAVY_MACHINERY"
    BICYCLE = "BICYCLE"
    QUAD_BIKE = "QUAD_BIKE"
    BOAT = "BOAT"
    OTHER = "OTHER"

class VehicleCondition(StrEnum):
    NEW = "NEW"
    USED = "USED"
    RECONDITIONED = "RECONDITIONED"

class VehicleStatus(StrEnum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    SOLD = "SOLD"
    EXPIRED = "EXPIRED"
    REMOVED = "REMOVED"

class FuelType(StrEnum):
    PETROL = "PETROL"
    DIESEL = "DIESEL"
    HYBRID = "HYBRID"
    ELECTRIC = "ELECTRIC"
    CNG = "CNG"
    LPG = "LPG"
    PEDAL = "PEDAL"
    OTHER = "OTHER"

class Transmission(StrEnum):
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"
    TIPTRONIC = "TIPTRONIC"
    CVT = "CVT"
    NONE = "NONE"

class MediaType(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"

class UserRole(StrEnum):
    ADMIN = "ADMIN"
    USER = "USER"