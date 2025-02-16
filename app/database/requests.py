from app.database.models import async_session
from app.database.models import Chat, Review
from sqlalchemy import select, insert

async def add_chat(chat_id: int) -> None:
    async with async_session() as session:
        chat = await session.scalar(select(Chat).where(Chat.id == chat_id))
        if not chat:
            session.add(Chat(id=chat_id))
            await session.commit()

async def save_review(user_id: int, bot: str, stars: int, text: str) -> None:
    async with async_session() as session:
        session.add(Review(user_id=user_id, bot=bot, stars=stars, text=text))
        await session.commit()

async def has_review(user_id: int, bot: str) -> bool:
    async with async_session() as session:
        review = await session.scalar(select(Review).where(Review.user_id == user_id, Review.bot == bot))
        if review:
            return True
        return False
