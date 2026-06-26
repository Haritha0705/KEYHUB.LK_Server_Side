from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    """Base schema for all API models.

    `from_attributes=True` lets response schemas be built directly from ORM
    objects via `Model.model_validate(orm_instance)`.
    """

    model_config = ConfigDict(from_attributes=True)

class IDMixin(BaseModel):
    id: UUID
