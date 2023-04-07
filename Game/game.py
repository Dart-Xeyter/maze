from field import Field


class Game:
    def __init__(self, player):
        self.player = player

    def game(self, arguments):
        side_length = self.player.get_field_size()
        field = Field(side_length, arguments)
        if arguments.show_field:
            print(field)
        row_index, column_index = self.player.get_start(side_length)
        self.player.cell = field[row_index][column_index]
        self.player.win = False
        self.player.send_message("Игра началась!")
        while self.player.win is False:
            self.make_move()

    def make_move(self):
        self.player.make_move()
