import config
from sqlalchemy import BIGINT, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url=config.sql_url)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Chat(Base):
    __tablename__ = 'chats'

    id = mapped_column(BIGINT, primary_key=True)


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id = mapped_column(BIGINT)
    bot: Mapped[str] = mapped_column(String(32))
    stars: Mapped[int] = mapped_column()
    text: Mapped[str] = mapped_column(String(4096))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
