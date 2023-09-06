class Player:
    def __init__(self, user_id=None):
        self.cell, self.win = None, False
        self.user_id = user_id

    async def make_move(self, logger):
        side = await logger.get_move(self)
        if self.cell.is_exit(side):
            self.win = True
            return
        if not self.cell.can_go(side):
            await logger.send_message(self, "Стенка")
        else:
            await logger.send_message(self, "Успешно")
            self.cell = self.cell.get_neighbour(side)
        self.cell = await self.cell.apply_effects(logger, self)
