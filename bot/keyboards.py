from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand
from aiogram import Bot

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/check")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start watching"),
        BotCommand(command="check", description="Check pool capacity"),
    ]
    
    await bot.set_my_commands(commands)
