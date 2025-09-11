from aiogram import Dispatcher, Bot
from config import BOT_TOKEN_API, PERIOD_SEC
from handlers import router, check_capacity
from keyboards import set_commands
from services.fetcher import init_fetcher, close_fetcher
import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


bot = Bot(BOT_TOKEN_API)
dp = Dispatcher()


async def main_loop(bot: Bot):
    while True:
        try:
            await check_capacity(bot)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
        await asyncio.sleep(PERIOD_SEC)


async def main_start():
    await init_fetcher()
    bot = Bot(BOT_TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router)

    await set_commands(bot)

    try:
        await asyncio.gather(
            dp.start_polling(bot),
            main_loop(bot)
        )
    finally:
        await close_fetcher()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main_start())

    