from Cell_Types.cell import Cell


class LandCell(Cell):
    def __str__(self):
        return '.'

    def __repr__(self):
        return super().__repr__()+' '+str(self)

    async def apply_effects(self, logger, player):
        return self
