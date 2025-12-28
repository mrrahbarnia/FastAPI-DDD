from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ..service.unit_of_work import SqlAlchemyUnitOfWork
from src.manager.dependencies.container import container

async_session_maker: async_sessionmaker[AsyncSession] = container.resolve(
    async_sessionmaker[AsyncSession]
)  # type: ignore


async def get_uow() -> SqlAlchemyUnitOfWork:
    return SqlAlchemyUnitOfWork()


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session_maker.begin() as session:
        yield session
