from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from config import MAX_CAPACITY, URL
from datetime import datetime, timezone

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
        if (pool.capacity is not None and pool.capacity < MAX_CAPACITY):
            result_message += '⚠️ '
        if (pool.capacity is not None and pool.capacity == 100):
            result_message += f'[{pool.token}] is full'
        elif pool.capacity is None:
            result_message += f'[{pool.token}]: parsing error' 
        else:
            result_message += f'[{pool.token}] is {pool.capacity}%'

        delta = datetime.now(tz=timezone.utc) - pool.update_time
        seconds = int(delta.total_seconds())

        result_message += f' ({seconds}s ago)\n'

    await message.answer(result_message)


async def check_capacity(bot: Bot):
    pools_to_alert = []
    for pool in pools:
        capacity: float = await fetch_width(pool.url)

        pool.capacity = capacity if capacity else pool.capacity

        if capacity is not None and capacity < MAX_CAPACITY:
            pools_to_alert.append(pool)

    if pools_to_alert:
        chats = get_chat_ids()
        await notify(
            bot=bot,
            chat_ids=chats,
            pools=pools_to_alert
        )