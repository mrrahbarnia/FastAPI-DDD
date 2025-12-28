# This is a shared dependency injector for all modules
import punq  # type: ignore
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)

from src.manager.config import ENVS
from src.app_book.adapters.notifications import INotification, EmailNotification


container = punq.Container()

ASYNC_ENGINE: AsyncEngine = create_async_engine(ENVS.POSTGRESQL.get_url)
SESSION_MAKER: async_sessionmaker[AsyncSession] = async_sessionmaker(
    ASYNC_ENGINE, expire_on_commit=False
)

container.register(INotification, EmailNotification)
container.register(AsyncEngine, instance=ASYNC_ENGINE)
container.register(async_sessionmaker[AsyncSession], instance=SESSION_MAKER)
