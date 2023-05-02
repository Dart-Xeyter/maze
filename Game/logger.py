from Cell_Types.cell import Cell


class Logger:
    def __init__(self, variant, bot):
        self.variant = variant
        self.bot = bot

    async def get_message(self, player):
        if self.variant == "terminal":
            return input()

    async def send_message(self, player, message, end='\n'):
        if not message:
            return
        if self.variant == "terminal":
            print(message, end=end)

    async def get_start(self, player, side_length):
        while True:
            try:
                await self.send_message(player, "Введите ваше начальное расположение: ", end='')
                message = await self.get_message(player)
                row_index, column_index = map(lambda x: int(x)-1, message.split())
                assert(-1 < min(row_index, column_index) and max(row_index, column_index) < side_length)
                return row_index, column_index
            except (ValueError, AssertionError):
                await self.send_message(player, "Некорректные координаты")

    async def get_move(self, player):
        commands = {'-': -1,
                    'u': Cell.sides.index('up'),
                    'r': Cell.sides.index('right'),
                    'd': Cell.sides.index('down'),
                    'l': Cell.sides.index('left')}
        while True:
            try:
                return commands[await self.get_message(player)]
            except KeyError:
                await self.send_message(player, "Некорректный ход")
