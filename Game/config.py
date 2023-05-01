from Cell_Types.cell import Cell
from Cell_Types.hole import HoleCell
from Cell_Types.water import WaterCell


def set_cell_configs():
    Cell.sides = ['up', 'right', 'down', 'left']
    Cell.side_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    HoleCell.state = "Вы попали в яму и провалились в следующую по циклу"

    WaterCell.minimum, WaterCell.maximum = 1, 2
    # maze may be impassable if WaterCell.minimum is more than 1
    WaterCell.states = ["исток", "реку", "устье"]
    WaterCell.state_action = f" и вас снесло на от {WaterCell.minimum} до {WaterCell.maximum} клеток по течению"
    WaterCell.state_destination = lambda self: f"Вы попали в {WaterCell.states[self.type]}"


max_number = 10
