from field import Field


class Game:
    def __init__(self, player):
        self.player = player

    def game(self, side_length, **kwargs):
        field = Field(side_length, **kwargs)
        row_index, column_index = self.player.get_start(side_length)
        self.player.cell = field[row_index][column_index]
        self.player.win = False
        while self.player.win is False:
            self.make_move()

    def make_move(self):
        self.player.make_move()
