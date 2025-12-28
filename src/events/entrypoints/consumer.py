import asyncio

from ..service.unit_of_work import IUnitOfWork, SqlAlchemyUnitOfWork
from ..service.messagebus import handle_event


async def process_event(uow: IUnitOfWork) -> None:
    # In production we have to processing events in batch
    async with uow:
        unprocessed_event = await uow.events.fetch_unprocessed()
        if unprocessed_event:
            await handle_event(
                event_type=unprocessed_event.event_type,
                payload=unprocessed_event.payload,
            )
            await uow.events.mark_processed(event_id=unprocessed_event.id)


async def main() -> None:
    sqlalchemy_uow = SqlAlchemyUnitOfWork()
    while True:
        await process_event(uow=sqlalchemy_uow)
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
