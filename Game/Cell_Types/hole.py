from Cell_Types.cell import Cell


class HoleCell(Cell):
    state = "Вы попали в яму и провалились в следующую по циклу"

    def __init__(self, row_index, column_index, field, index):
        super().__init__(row_index, column_index, field)
        self.next, self.index = self, index

    def __str__(self):
        return str(self.index)

    def __repr__(self):
        return super().__repr__()+' '+str(self)

    def apply_effects(self, player):
        player.send_message(HoleCell.state)
        return self.next
