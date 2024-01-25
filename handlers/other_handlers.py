from aiogram import Router
from aiogram.types import Message
from services.services import send_weather

router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=str(await send_weather(message)))
