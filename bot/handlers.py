from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from config import MAX_CAPACITY, URL

from services.notifier import notify, create_notification_text
from services.storage import get_chat_ids, add_chat_id
from services.fetcher import fetch_width

from models.tokens import pools

from keyboards import main_kb

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    add_chat_id(message.chat.id)
    await message.answer(
        '👋 Hello! I\'m Crypto Watchdog, now I\'m watching for Exponent xSOL pool\n\n'
        '💸 I will tell you about changes in the pool or you can write command /check to get current pool capacity right now',
        reply_markup=main_kb
    )


@router.message(Command('check'))
async def cmd_check(message: Message):
    result_message = 'Current pools capacity\n\n'
    for pool in pools:
        width: str = await fetch_width(pool.url)
        if width is None:
            await message.answer("Cannot fetch capacity")
            return
    
        curr_capacity = float(width.rstrip('%'))
        pool.capacity = curr_capacity

        if (curr_capacity < MAX_CAPACITY):
            result_message += '⚠️ '
        result_message += f'[{pool.token}] is {curr_capacity}%\n'

    await message.answer(result_message)


async def check_capacity(bot: Bot):
    pools_to_alert = []
    for pool in pools:
        width: str = await fetch_width(pool.url)
        curr_capacity = float(width.rstrip('%'))
        pool.capacity = curr_capacity
        if curr_capacity <= MAX_CAPACITY:
            pools_to_alert.append(pool)

    if pools_to_alert:
        chats = get_chat_ids()
        await notify(
            bot=bot,
            chat_ids=chats,
            pools=pools_to_alert
        )