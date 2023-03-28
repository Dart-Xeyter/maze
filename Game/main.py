from game import Game
from player import Player


if __name__ == "__main__":
    game = Game(Player())
    play = True
    while play:
        side_length = int(input("Введите размер поля: "))
        game.game(side_length)
        verdict = input("Начать новую игру? ")
        while verdict not in ['y', 'n']:
            verdict = input("Некорректный ответ\n")
        play = (verdict == 'y')
