from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from config import Config


engine = create_async_engine(url=Config.DATABASE_URL, echo=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    from sqlmodel.ext.asyncio.session import AsyncSession

    async with AsyncSession(engine) as session:
        yield session
