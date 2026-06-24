import math

from src.app.schemas.pagination import PaginationMeta

def build_pagination_meta(page: int, page_size: int, total_items: int) -> PaginationMeta:

    total_pages = math.ceil(total_items / page_size)

    return PaginationMeta(
        page=page,
        page_size=page_size,
        total_items=total_items,
        total_pages=total_pages,
        has_next = page < total_pages,
        has_previous = page > 1
    )