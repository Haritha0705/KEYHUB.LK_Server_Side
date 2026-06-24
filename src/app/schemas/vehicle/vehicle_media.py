from sqlmodel import Field

from src.app.models.common import MediaType
from src.app.schemas.base import Base, IDMixin

class VehicleMediaRequest(Base):

    url: str = Field(min_length=1, max_length=500)

    media_type: MediaType = MediaType.IMAGE

    is_primary: bool = False

    position: int = Field(default=0, ge=0)

class VehicleMediaResponse(IDMixin, Base):

    url: str

    media_type: MediaType

    is_primary: bool

    position: int
