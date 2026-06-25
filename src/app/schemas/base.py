from uuid import UUID
from pydantic import BaseModel

class Base(BaseModel):
    pass

class IDMixin(BaseModel):
    id: UUID