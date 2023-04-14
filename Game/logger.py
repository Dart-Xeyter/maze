from Cell_Types.cell import Cell


class Logger:
    def __init__(self, variant):
        self.variant = variant

    def get_message(self):
        if self.variant == "terminal":
            return input()

    def send_message(self, message, end='\n'):
        if not message:
            return
        if self.variant == "terminal":
            print(message, end=end)

    def get_start(self, side_length):
        while True:
            try:
                self.send_message("Введите ваше начальное расположение: ", end='')
                row_index, column_index = map(lambda x: int(x)-1, self.get_message().split())
                assert(-1 < min(row_index, column_index) and max(row_index, column_index) < side_length)
                return row_index, column_index
            except (ValueError, AssertionError):
                self.send_message("Некорректные координаты")

    def get_move(self):
        commands = {'-': -1,
                    'u': Cell.sides.index('up'),
                    'r': Cell.sides.index('right'),
                    'd': Cell.sides.index('down'),
                    'l': Cell.sides.index('left')}
        while True:
            try:
                return commands[self.get_message()]
            except KeyError:
                self.send_message("Некорректный ход")
