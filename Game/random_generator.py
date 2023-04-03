import random
from Cell_Types.land import LandCell


def randint(minimum, maximum):
    return random.randint(minimum, maximum)


def choice(collection):
    return random.choice(collection)


def get_random_cell(field):
    candidates = []
    for row in field:
        for cell in row:
            if type(cell) == LandCell:
                candidates.append(cell)
    return choice(candidates)


def get_random_neighbour(cell):
    candidates = [side for side in range(0, 4) if cell.get_neighbour(side) is not None]
    return choice(candidates) if len(candidates) != 0 else None
