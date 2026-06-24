import uuid
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from sqlmodel import DateTime, func
from enum import StrEnum

def _utcnow() -> datetime:
    return datetime.now(timezone.utc)

class TimestampMixin:

    created_at: datetime = Field(
        default_factory=_utcnow,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now()},
        nullable=False,
    )

    updated_at: datetime = Field(
        default_factory=_utcnow,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()},
        nullable=False,
    )

class BaseModel(SQLModel, TimestampMixin):

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

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
