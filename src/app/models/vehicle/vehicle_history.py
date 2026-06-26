from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import Integer, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.vehicle.base import VehicleSubBase
if TYPE_CHECKING:
    from src.app.models.vehicle.vehicle import Vehicle

class VehicleHistory(VehicleSubBase):

    __tablename__ = "vehicle_history"

    previous_owners: Mapped[int] = mapped_column(Integer, default=0)
    had_accidents: Mapped[bool] = mapped_column(Boolean, default=False)
    accident_history: Mapped[str | None] = mapped_column(Text)
    service_history: Mapped[str | None] = mapped_column(Text)
    import_details: Mapped[str | None] = mapped_column(Text)

    # ONE-TO-ONE RELATIONSHIPS

    vehicle: Mapped[Vehicle] = relationship(back_populates="history")