from Cell_Types.cell import Cell


class LandCell(Cell):
    def __str__(self):
        return '.'

    def __repr__(self):
        return super().__repr__()+' '+str(self)

    def apply_effects(self, player):
        return self
