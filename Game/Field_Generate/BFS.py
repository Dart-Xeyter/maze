from queue import Queue
from Cell_Types.land import LandCell
from Cell_Types.water import WaterCell


def is_connected(self, cell):
    n = self.side_length
    was = [[False]*n for _ in range(n)]
    queue = Queue()
    queue.put(cell)
    was[cell.row_index][cell.column_index] = True
    while not queue.empty():
        cell = queue.get()
        if not isinstance(cell, LandCell) and not was[cell.next.row_index][cell.next.column_index]:
            queue.put(cell.next)
            was[cell.next.row_index][cell.next.column_index] = True
        for side in range(4):
            if cell.can_go(side) and not cell.is_exit(side):
                neighbour = cell.get_neighbour(side)
                if not (isinstance(neighbour, WaterCell) and neighbour.next == cell) and \
                        not was[neighbour.row_index][neighbour.column_index]:
                    queue.put(neighbour)
                    was[neighbour.row_index][neighbour.column_index] = True
    return all(all(q for q in row) for row in was)
