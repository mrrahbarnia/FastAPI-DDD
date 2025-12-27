from pydantic import BaseModel

from ...domain.models import BookStatusEnum
from src.manager.common.types import BookID
from src.manager.common.pagination_schema import PaginationSchema


class CreateBookRequest(BaseModel):
    title: str


class CreateBookResponse(CreateBookRequest):
    id: BookID


class BookListQueryParams(PaginationSchema):
    title__icontain: str | None = None


class BookRead(BaseModel):
    id: BookID
    title: str
    status: BookStatusEnum
    borrow_count: int
