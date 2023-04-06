class Player:
    def __init__(self):
        self.cell = self.win = None

    def get_start(self, side_length):
        while True:
            try:
                row_index, column_index = map(lambda x: int(x)-1, self.get_message().split())
                assert(-1 < min(row_index, column_index) and max(row_index, column_index) < side_length)
                return row_index, column_index
            except (ValueError, AssertionError):
                self.send_message("Некорректные координаты")

    def get_move(self):
        commands = {'-': -1, 'u': 0, 'r': 1, 'd': 2, 'l': 3}
        while True:
            try:
                return commands[self.get_message()]
            except KeyError:
                self.send_message("Некорректный ход")

    def make_move(self):
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]
        side = self.get_move()
        row_index = self.cell.row_index+moves[side][0]
        column_index = self.cell.column_index+moves[side][1]
        if side != -1 and self.cell.is_exit(side):
            self.send_message("Поздравляем, вы вышли из лабиринта!")
            self.win = True
            return
        if side != -1 and not self.cell.can_go(side):
            self.send_message("Стенка")
        else:
            self.send_message("Успешно")
            self.cell = self.cell.field[row_index][column_index]
        self.cell = self.cell.apply_effects(self)

    def get_message(self):
        return input()

    def send_message(self, message):
        if message:
            print(message)
