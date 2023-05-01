import config
from arguments import Arguments
from game import Game
from player import Player
from sys import argv, exit


if __name__ == "__main__":
    arguments = Arguments(argv)
    game = Game(tuple(Player("terminal") for _ in range(arguments.num_players)))
    if not arguments.repeat:
        game.game(arguments)
        exit(0)
    play = True
    while play:
        game.game(arguments)
        verdict = input("Начать новую игру? ")
        while verdict not in ['y', 'n']:
            verdict = input("Некорректный ответ\n")
        play = (verdict == 'y')
