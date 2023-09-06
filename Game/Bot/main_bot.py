from aiogram import bot, dispatcher, types
from aiogram.utils import executor
from config import bot_help, set_cell_configs
from Bot.game_bot import main
from Bot.logger_bot import messages
from config import TOKEN
bot = bot.Bot(TOKEN)
dp = dispatcher.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hola :)")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(bot_help, parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(commands=['game'])
async def game_command(message: types.Message):
    user_id = message.from_user.id
    if not await main(bot, message.text, user_id):
        await message.reply("Подождите немного, идёт поиск игроков...")


@dp.message_handler()
async def player_move(message: types.Message):
    user_id = message.from_user.id
    messages[user_id] = message


if __name__ == '__main__':
    set_cell_configs()
    executor.start_polling(dp)
