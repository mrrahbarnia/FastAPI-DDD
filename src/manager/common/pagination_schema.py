from typing import Annotated, NewType, Literal, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")

Limit = NewType("Limit", int)
Offset = NewType("Offset", int)


class PaginationSchema(BaseModel):
    current_page: Annotated[int, Field(ge=1)] = 1
    page_size: Annotated[int, Field(ge=1)] = 10
    sort_mode: Literal["ASC", "DESC"] = "DESC"

    def to_limit_offset(self) -> tuple[Limit, Offset]:
        limit = self.page_size
        offset = (self.current_page - 1) * self.page_size
        return Limit(limit), Offset(offset)


class PaginationResponse(BaseModel):
    current_page: int
    page_size: int
    total: int


class PaginationResponseSchema(BaseModel, Generic[T]):
    pagination: PaginationResponse
    data: T
