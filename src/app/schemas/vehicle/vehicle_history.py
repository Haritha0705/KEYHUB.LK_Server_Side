from pydantic import Field
from src.app.schemas.base import Base, IDMixin

class VehicleHistoryBase(Base):
    accident_history: str | None = None
    service_history: str | None = None
    import_details: str | None = None

class VehicleHistoryRequest(VehicleHistoryBase):
    previous_owners: int = Field(default=0, ge=0)
    had_accidents: bool = False

class VehicleHistoryResponse(IDMixin, VehicleHistoryBase):
    previous_owners: int
    had_accidents: bool
