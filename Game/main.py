from arguments import arguments
from config import set_cell_configs
from game import Game
from player import Player


if __name__ == "__main__":
    set_cell_configs()
    game = Game(tuple(Player("terminal") for _ in range(arguments.num_players)))
    game.game(arguments)
