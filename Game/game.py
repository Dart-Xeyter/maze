from field import Field
from random_generator import set_seed


class Game:
    def __init__(self, players):
        self.players = players
        self.who_moves = 0

    def game(self, arguments):
        if arguments.debug:
            set_seed()
        side_length = arguments.side_length
        field = Field(side_length, arguments)
        for player in self.players:
            row_index, column_index = player.logger.get_start(side_length)
            player.cell = field[row_index][column_index]
        if arguments.show_field:
            print(field)
        for player in self.players:
            player.logger.send_message("Игра началась!")
        while all(not player.win for player in self.players):
            self.make_move()
        for player in self.players:
            player.logger.send_message("Поздравляем, вы вышли из лабиринта!"
                                       if player.win else
                                       "К сожалению, другой игрок опередил вас :(")

    def make_move(self):
        self.players[self.who_moves].make_move()
        self.who_moves = (self.who_moves+1) % len(self.players)
