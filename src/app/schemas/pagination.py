from sqlmodel import SQLModel
from typing import Generic, TypeVar

T = TypeVar("T")

class PaginationMeta(SQLModel):

    page: int

    page_size: int

    total_items: int

    total_pages: int

    has_next: bool

    has_previous: bool

class PaginatedResponse(SQLModel, Generic[T]):

    data: list[T]

    meta: PaginationMeta