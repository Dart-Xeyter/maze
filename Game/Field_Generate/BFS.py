from queue import Queue
from Cell_Types.land import LandCell
from Cell_Types.water import WaterCell


def add_vertex(cell, queue, was):
    queue.put(cell)
    was[cell.row_index][cell.column_index] = True


def add_next(cell, queue, was):
    if not isinstance(cell, LandCell) and \
            not was[cell.next.row_index][cell.next.column_index]:
        add_vertex(cell.next, queue, was)


def add_neighbour(cell, neighbour, queue, was):
    if not (isinstance(neighbour, WaterCell) and neighbour.next == cell) and \
            not was[neighbour.row_index][neighbour.column_index]:
        add_vertex(neighbour, queue, was)


def check_termination(cell):
    return isinstance(cell, WaterCell) and cell.type == 0


def is_connected(self, cell):
    n = self.side_length
    was = [[False]*n for _ in range(n)]
    queue = Queue()
    add_vertex(cell, queue, was)
    while not queue.empty():
        cell = queue.get()
        add_next(cell, queue, was)
        if check_termination(cell):
            continue
        for side in range(4):
            if cell.can_go(side) and not cell.is_exit(side):
                add_neighbour(cell, cell.get_neighbour(side), queue, was)
    return all(all(was_there for was_there in row) for row in was)
