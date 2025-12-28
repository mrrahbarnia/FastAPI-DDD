from typing import Protocol, Self

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
)

from ..adapters.repository import (
    IRepository as EventIRepository,
    SqlAlchemyRepository as EventSqlAlchemyRepository,
)
from src.manager.dependencies.container import container


async_session_maker: async_sessionmaker[AsyncSession] = container.resolve(
    async_sessionmaker[AsyncSession]
)  # type: ignore


class IUnitOfWork(Protocol):
    events: EventIRepository

    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback,
    ) -> None: ...


class SqlAlchemyUnitOfWork:
    events: EventIRepository

    def __init__(self, session_maker=async_session_maker) -> None:
        self.session_maker = session_maker

    async def __aenter__(self) -> Self:
        session = self.session_maker()
        self.events = EventSqlAlchemyRepository(session)
        self.session = session
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback,
    ) -> None:
        try:
            if exc_type is not None:
                await self.rollback()
            else:
                await self.commit()
        finally:
            await self.session.close()

    async def rollback(self):
        return await self.session.rollback()

    async def commit(self):
        return await self.session.commit()


class FakeUnitOfWork:
    # For testing
    ...
