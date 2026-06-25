from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.vehicle.base import VehicleSubBase

if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleDocuments(VehicleSubBase, table=True):

    __tablename__ = "vehicle_documents"

    registration_number: Mapped[str | None] = mapped_column(String(30), unique=True)
    chassis_number: Mapped[str | None] = mapped_column(String(50))
    engine_number: Mapped[str | None] = mapped_column(String(50))
    insurance_company: Mapped[str | None] = mapped_column(String(100))
    insurance_expiry: Mapped[date | None] = mapped_column(Date)
    revenue_license_expiry: Mapped[date | None] = mapped_column(Date)
    emission_test_expiry: Mapped[date | None] = mapped_column(Date)
    license_status: Mapped[str | None] = mapped_column(String(20))

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: Mapped[Vehicle] = relationship(back_populates="documents")