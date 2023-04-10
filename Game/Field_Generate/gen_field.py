from border import Border
from Cell_Types.land import LandCell


def generate_empty_field(self):
    n = self.side_length
    self.field = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            self.field[i].append(LandCell(i, j, self))


def generate_basic_borders(self):
    n = self.side_length
    self.rows = [[] for _ in range(n)]
    self.columns = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n + 1):
            self.rows[i].append(Border(0 < j < n, False))
            self.columns[i].append(Border(0 < j < n, False))
