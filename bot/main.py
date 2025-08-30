from aiogram import Dispatcher, Bot
from config import BOT_TOKEN_API, PERIOD_SEC
from handlers import router, check_capacity
from keyboards import set_commands
import asyncio


bot = Bot(BOT_TOKEN_API)
dp = Dispatcher()


async def main_loop():
    while True:
        await check_capacity(bot)
        await asyncio.sleep(PERIOD_SEC)


async def main_start():
    await set_commands(bot)

    dp.include_router(router)
    await asyncio.gather(
        dp.start_polling(bot),
        main_loop()
    )


if __name__ == '__main__':
    asyncio.run(main_start())

    