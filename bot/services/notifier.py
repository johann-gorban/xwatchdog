from time import time
from typing import List
from .config import ALERT_COOLDOWN_SEC
from aiogram import Bot

last_notification_time = 0

async def notify(bot: Bot, chat_ids: List[str | int], curr_capacity: float):
    global last_notification_time
    now = time()
    if now - last_notification_time > ALERT_COOLDOWN_SEC:
        for id in chat_ids:
            await bot.send_message(
                chat_id=id,
                text=f'⚠️ Pool capacity now is {curr_capacity}% ⚠️'
            )

        last_notification_time = now
