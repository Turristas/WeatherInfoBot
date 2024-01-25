import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import users_handlers, other_handlers

# Инициализируем Logger
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def bot_log():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    # Registration router в диспетчере
    dp.include_router(users_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся updates и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(bot_log())
