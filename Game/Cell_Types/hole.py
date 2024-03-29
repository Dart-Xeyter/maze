from Cell_Types.cell import Cell


class HoleCell(Cell):
    def __init__(self, row_index, column_index, field, index):
        super().__init__(row_index, column_index, field)
        self.next, self.index = self, index

    def __str__(self):
        return str(self.index+1)

    def __repr__(self):
        return super().__repr__()+' '+str(self)

    async def apply_effects(self, logger, player):
        await logger.send_message(player, HoleCell.state)
        return self.next
