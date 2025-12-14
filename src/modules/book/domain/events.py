from dataclasses import dataclass

from src.common import types


@dataclass(frozen=True)
class BookBorrowed(types.Event):
    id: types.BookID
    title: str


@dataclass(frozen=True)
class BookReturned(types.Event):
    id: types.BookID
    title: str
