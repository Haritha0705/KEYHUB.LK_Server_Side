from datetime import date

from src.app.schemas.base import Base, IDMixin

class VehicleDocumentsBase(Base):

    registration_number: str | None = None
    chassis_number: str | None = None
    engine_number: str | None = None
    insurance_company: str | None = None
    insurance_expiry: date | None = None
    revenue_license_expiry: date | None = None

class VehicleDocumentsRequest(VehicleDocumentsBase):
    pass

class VehicleDocumentsResponse(IDMixin, VehicleDocumentsBase):
    pass