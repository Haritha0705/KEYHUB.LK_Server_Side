import enum


class VehicleType(str, enum.Enum):
    """Adjust these to match exactly what your VehicleType schema expects."""
    CAR = "CAR"
    MOTORCYCLE = "MOTORCYCLE"
    THREE_WHEELER = "THREE_WHEELER"   # tuk-tuk, common in the SL market
    VAN = "VAN"
    SUV = "SUV"
    PICKUP = "PICKUP"
    BUS = "BUS"
    LORRY = "LORRY"
    OTHER = "OTHER"


class VehicleCondition(str, enum.Enum):
    NEW = "NEW"
    USED = "USED"
    RECONDITIONED = "RECONDITIONED"   # very common category in Sri Lanka


class VehicleStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    SOLD = "SOLD"
    INACTIVE = "INACTIVE"
