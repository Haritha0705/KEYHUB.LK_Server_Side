import uuid
from sqlmodel import Field

from src.app.models.common import BaseModel

class VehicleSubBase(BaseModel):

    vehicle_id: uuid.UUID = Field(foreign_key="vehicle.id", ondelete="CASCADE")
