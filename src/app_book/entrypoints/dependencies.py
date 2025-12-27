from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import AsyncConnection

from ..service.unit_of_work import SqlAlchemyUnitOfWork, ASYNC_ENGINE


async def get_uow() -> SqlAlchemyUnitOfWork:
    return SqlAlchemyUnitOfWork()


async def get_session() -> AsyncGenerator[AsyncConnection, Any]:
    connection = ASYNC_ENGINE.connect()
    try:
        yield connection
    finally:
        await connection.close()
