from datetime import date
from typing import TYPE_CHECKING
from sqlmodel import Field, String, Date, Relationship

from src.app.models.vehicle.base import VehicleSubBase

if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleDocuments(VehicleSubBase, table=True):

    __tablename__ = "vehicle_document"

    registration_number: str | None = Field(default=None, sa_type=String(30), unique=True)

    chassis_number: str | None = Field(default=None, sa_type=String(50), nullable=True)

    engine_number: str | None = Field(default=None, sa_type=String(50), nullable=True)

    insurance_company: str | None = Field(default=None, sa_type=String(100), nullable=True)

    insurance_expiry: date | None = Field(default=None, sa_type=Date, nullable=True)

    revenue_license_expiry: date | None = Field(default=None, sa_type=Date, nullable=True)

    emission_test_expiry: date | None = Field(default=None, sa_type=Date, nullable=True)

    license_status: str | None = Field(default=None, sa_type=String(20), nullable=True)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: "Vehicle" = Relationship(back_populates="documents")