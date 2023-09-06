class Cell:
    def __init__(self, row_index, column_index, field):
        self.row_index, self.column_index = row_index, column_index
        self.field = field

    def __repr__(self):
        return f'({self.row_index}, {self.column_index})'

    def get_border(self, side):
        if side % 2 == 1:
            return self.field.rows[self.row_index][self.column_index+(side == 1)]
        return self.field.columns[self.column_index][self.row_index+(side == 2)]

    def get_neighbour(self, side):
        if side == -1:
            return self
        row_coordinate = self.row_index+Cell.side_directions[side][0]
        column_coordinate = self.column_index+Cell.side_directions[side][1]
        if not (0 <= row_coordinate < self.field.side_length and 0 <= column_coordinate < self.field.side_length):
            return None
        return self.field[row_coordinate][column_coordinate]

    def can_go(self, side):
        return side == -1 or self.get_border(side).can_go

    def is_exit(self, side):
        return side != -1 and self.get_border(side).is_exit
