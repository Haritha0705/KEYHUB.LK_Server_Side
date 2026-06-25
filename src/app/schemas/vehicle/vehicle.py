from datetime import datetime
from pydantic import Field

from src.app.schemas.base import Base, IDMixin
from src.app.models.common import VehicleType, VehicleCondition, VehicleStatus
from src.app.schemas.vehicle.vehicle_documents import VehicleDocumentsRequest, VehicleDocumentsResponse
from src.app.schemas.vehicle.vehicle_history import VehicleHistoryRequest, VehicleHistoryResponse
from src.app.schemas.vehicle.vehicle_media import VehicleMediaRequest, VehicleMediaResponse
from src.app.schemas.vehicle.vehicle_pricing import VehiclePricingRequest, VehiclePricingResponse
from src.app.schemas.vehicle.vehicle_specs import VehicleSpecsRequest, VehicleSpecsResponse

class VehicleBase(Base):
    vehicle_type: VehicleType
    description: str | None = None

class VehicleResponseBase(IDMixin, VehicleBase):
    title: str
    make: str | None = None
    model: str | None = None
    trim: str | None = None
    year_of_manufacture: int | None = None
    condition: VehicleCondition
    status: VehicleStatus
    district: str | None = None
    city: str | None = None
    is_featured: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

class VehicleCommon(Base):
    make: str | None = Field(None, max_length=50)
    model: str | None = Field(None, max_length=50)
    trim: str | None = Field(None, max_length=50)
    district: str | None = None
    city: str | None = None

class VehicleRequest(VehicleBase, VehicleCommon):
    title: str = Field(min_length=3, max_length=150)
    year_of_manufacture: int | None = Field(None, ge=1900, le=2100)
    condition: VehicleCondition = VehicleCondition.USED
    status: VehicleStatus
    is_featured: bool = False
    is_verified: bool = False

    # Relations (optional recommended)
    specs: VehicleSpecsRequest | None = None
    pricing: VehiclePricingRequest | None = None
    documents: VehicleDocumentsRequest | None = None
    history: VehicleHistoryRequest | None = None
    media: list[VehicleMediaRequest] = Field(default_factory=list)

class VehicleResponse(VehicleResponseBase):
    # Relations
    specs: VehicleSpecsResponse | None = None
    pricing: VehiclePricingResponse | None = None
    history: VehicleHistoryResponse | None = None
    documents: VehicleDocumentsResponse | None = None
    media: list[VehicleMediaResponse] = Field(default_factory=list)

class VehicleListResponse(VehicleResponseBase):
    # Relations
    pricing: VehiclePricingResponse | None = None
    specs: VehicleSpecsResponse | None = None
    media: list[VehicleMediaResponse] = Field(default_factory=list)

class VehicleUpdateRequest(VehicleCommon):
    title: str | None = Field(default=None, min_length=3, max_length=150)
    description: str | None = None
    year_of_manufacture: int | None = Field(default=None, ge=1900, le=2100)
    condition: VehicleCondition | None = None
    status: VehicleStatus | None = None
    is_featured: bool | None = None
    is_verified: bool | None = None
