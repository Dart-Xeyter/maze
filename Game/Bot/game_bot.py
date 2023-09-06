from arguments import get_arguments
from game import Game
from Bot.logger_bot import incipient_games
from player import Player


async def main(bot, argv, user_id):
    arguments = get_arguments(argv.split()[1:])
    str_arguments = str(arguments)
    if str_arguments not in incipient_games:
        incipient_games[str_arguments] = []
    incipient_games[str_arguments].append(user_id)
    if len(incipient_games[str_arguments]) < arguments.num_players:
        return False
    game = Game("telegram", tuple(Player(user_id) for user_id in incipient_games[str_arguments]), bot)
    await game.game(arguments)
    del incipient_games[str_arguments]
    return True
