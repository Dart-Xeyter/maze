import asyncio
from arguments import get_arguments
from config import set_cell_configs
from game import Game
from player import Player


async def main():
    arguments = get_arguments()
    game = Game("terminal", tuple(Player() for _ in range(arguments.num_players)))
    await game.game(arguments)


if __name__ == "__main__":
    set_cell_configs()
    asyncio.run(main())
