from aiogram import types
from asyncio import sleep
from config import delay


async def get_message(player):
    while player.user_id not in messages:
        await sleep(delay)
    text = messages[player.user_id].text
    del messages[player.user_id]
    return text


async def send_message(bot, player, message):
    await bot.send_message(player.user_id, message, parse_mode=types.ParseMode.MARKDOWN)


incipient_games = {}
messages = {}
