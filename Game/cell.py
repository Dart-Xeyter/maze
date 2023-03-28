class Cell:
    def __init__(self, row_index, column_index, field):
        self.row_index, self.column_index = row_index, column_index
        self.field = field

    def get_border(self, side):
        # Cell has 4 sides - [up, right, down, left]
        if side % 2 == 1:
            return self.field.columns[self.column_index][self.row_index+(side == 3)]
        return self.field.rows[self.row_index][self.column_index+(side == 2)]

    def can_go(self, side):
        return self.get_border(side).can_go

    def is_exit(self, side):
        return self.get_border(side).is_exit


class EmptyCell(Cell):
    state = ""

    def apply_effects(self):
        return self
