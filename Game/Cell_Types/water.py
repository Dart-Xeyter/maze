from Cell_Types.cell import Cell
from random_generator import randint


class WaterCell(Cell):
    minimum, maximum = 1, 2
    states = ["исток", "реку", "устье"]
    state_action = f" и вас снесло на от {minimum} до {maximum} клеток по течению"

    def __init__(self, row_index, column_index, field, type=1):
        super().__init__(row_index, column_index, field)
        self.next, self.type = self, type

    def __str__(self):
        return 'И' if self.type == 0 else 'У' if self.type == 2 else 'В'

    def __repr__(self):
        return super().__repr__()+' '+str(self)

    def state_destination(self):
        return f"Вы попали в {WaterCell.states[self.type]}"

    def apply_effects(self, logger):
        if self.type == 2:
            logger.send_message(self.state_destination())
            return self
        logger.send_message(self.state_destination()+WaterCell.state_action)
        final_cell = self
        for q in range(randint(WaterCell.minimum, WaterCell.maximum)):
            final_cell = final_cell.next
        if final_cell.type == 2:
            logger.send_message(final_cell.state_destination())
        return final_cell
