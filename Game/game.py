from field import Field
from logger import Logger
from random_generator import set_seed


class Game:
    def __init__(self, variant, players, bot=None):
        self.logger = Logger(variant, bot)
        self.players = players
        self.who_moves = 0

    async def game(self, arguments):
        if arguments.debug:
            set_seed()
        side_length = arguments.side_length
        field = Field(side_length, arguments)
        for player in self.players:
            row_index, column_index = await self.logger.get_start(player, side_length)
            player.cell = field[row_index][column_index]
        if arguments.show_field:
            for player in self.players:
                await self.logger.send_message(player, str(field))
        for player in self.players:
            await self.logger.send_message(player, "Игра началась!")
        while all(not player.win for player in self.players):
            await self.make_move()
        for player in self.players:
            await self.logger.send_message(player, "Поздравляем, вы вышли из лабиринта!"
                                              if player.win else
                                             "К сожалению, другой игрок опередил вас :(")

    async def make_move(self):
        await self.players[self.who_moves].make_move(self.logger)
        self.who_moves = (self.who_moves+1) % len(self.players)
