class Cell:
    # Cell has 4 sides - [up, right, down, left]
    sides = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, row_index, column_index, field):
        self.row_index, self.column_index = row_index, column_index
        self.field = field

    def get_border(self, side):
        if side % 2 == 1:
            return self.field.columns[self.column_index][self.row_index+(side == 3)]
        return self.field.rows[self.row_index][self.column_index+(side == 2)]

    def get_neighbour(self, side):
        row_coordinate = self.row_index+Cell.sides[side][0]
        column_coordinate = self.column_index+Cell.sides[side][1]
        if not (0 <= row_coordinate < self.field.side_length and 0 <= column_coordinate < self.field.side_length):
            return None
        return self.field[row_coordinate][column_coordinate]

    def can_go(self, side):
        return self.get_border(side).can_go

    def is_exit(self, side):
        return self.get_border(side).is_exit
