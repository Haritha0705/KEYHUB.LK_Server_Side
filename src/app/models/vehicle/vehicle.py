from sqlalchemy import Boolean, String, Enum, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.vehicle.vehicle_documents import VehicleDocuments
from src.app.models.vehicle.vehicle_history import VehicleHistory
from src.app.models.vehicle.vehicle_media import VehicleMedia
from src.app.models.vehicle.vehicle_pricing import VehiclePricing
from src.app.models.vehicle.vehicle_specs import VehicleSpecs
from src.app.models.common import BaseModel, VehicleType, VehicleCondition, VehicleStatus

class Vehicle(BaseModel):

    __tablename__ = "vehicles"

    vehicle_type: Mapped[VehicleType] = mapped_column(Enum(VehicleType, name="vehicle_type"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    make: Mapped[str | None] = mapped_column(String(50), index=True)
    model: Mapped[str | None] = mapped_column(String(50), index=True)
    trim: Mapped[str | None] = mapped_column(String(50))
    year_of_manufacture: Mapped[int | None] = mapped_column(Integer, index=True)
    condition: Mapped[VehicleCondition] = mapped_column(Enum(VehicleCondition, name="vehicle_condition"),default=VehicleCondition.USED)
    status: Mapped[VehicleStatus] = mapped_column(Enum(VehicleStatus, name="vehicle_status"),default=VehicleStatus.DRAFT,index=True)
    district: Mapped[str | None] = mapped_column(String(50), index=True)
    city: Mapped[str | None] = mapped_column(String(50), index=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    # ONE-TO-ONE RELATIONSHIPS

    specs: Mapped[VehicleSpecs] = relationship(back_populates="vehicle",uselist=False,cascade="all, delete-orphan")
    documents: Mapped[VehicleDocuments] = relationship(back_populates="vehicle",uselist=False,cascade="all, delete-orphan")
    pricing: Mapped[VehiclePricing] = relationship(back_populates="vehicle",uselist=False,cascade="all, delete-orphan")
    history: Mapped[VehicleHistory] = relationship(back_populates="vehicle",uselist=False,cascade="all, delete-orphan")

    # ONE-TO-MANY RELATIONSHIP

    media: Mapped[list[VehicleMedia]] = relationship(back_populates="vehicle",cascade="all, delete-orphan",order_by="VehicleMedia.position")

    # Index

