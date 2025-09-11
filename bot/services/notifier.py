from time import time
from typing import List
from models.tokens import Pool
from .config import ALERT_COOLDOWN_SEC
from aiogram import Bot
from datetime import timedelta, datetime, timezone

last_notification_time = 0

def create_notification_text(pools: List[Pool]) -> str:
    notification = 'New update:\n\n'
    for pool in pools:
        delta = datetime.now(tz=timezone.utc) - pool.update_time
        seconds = int(delta.total_seconds())

        if pool.capacity is not None:
            notification += f'[{pool.token}]: {pool.capacity}%'
        else:
            notification += f'[{pool.token}]: parsing error'
        
        notification += f' ({seconds}s ago)'
        notification += '\n'
        
    return notification


async def notify(bot: Bot, chat_ids: List[str | int], pools: List[Pool]):
    global last_notification_time
    now = time()
    if now - last_notification_time > ALERT_COOLDOWN_SEC:
        notification_text = create_notification_text(pools)
        for id in chat_ids:
            await bot.send_message(
                chat_id=id,
                text=notification_text
            )

        last_notification_time = now
