from Cell_Types.cell import Cell


class HoleCell(Cell):
    state = "Вы попали в яму и провалились в следующую по циклу"

    def __init__(self, row_index, column_index, field):
        super().__init__(row_index, column_index, field)
        self.next = self

    def apply_effects(self, player):
        player.send_message(HoleCell.state)
        return self.next
