from uuid import UUID
from sqlmodel import SQLModel

class Base(SQLModel):

    pass

class IDMixin(SQLModel):

    id: UUID