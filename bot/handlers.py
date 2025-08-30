from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from fetcher import fetch_width
from config import MAX_CAPACITY, URL
from notifier import notify

router = Router()

chat_ids = set()

@router.message(Command('start'))
async def cmd_start(message: Message):
    chat_ids.add(message.chat.id)
    await message.answer(
        'Hello! I\'m Crypto Watchdog, now I\'m watching for Exponent xSOL pool\n\n'
        'I will tell you about changes in the pool or you can write command /check to get current pool capacity right now'
    )


@router.message(Command('check'))
async def cmd_check(message: Message):
    width: str = await fetch_width(URL)
    if width is None:
        await message.answer("Cannot fetch capacity")
        return
    
    curr_capacity = float(width.rstrip('%'))
    if (curr_capacity >= MAX_CAPACITY):
        await message.answer(text=f'💤 Pool capacity now is {curr_capacity}%')
    else:
        await message.answer(text=f'⚠️ Pool capacity now is {curr_capacity}%')


async def check_capacity(bot: Bot):
    width: str = await fetch_width(URL)
    curr_capacity = float(width.rstrip('%'))
    if curr_capacity <= MAX_CAPACITY:
        await notify(
            bot=bot,
            chat_ids=chat_ids,
            curr_capacity=curr_capacity
        )