from logger import Logger


class Player:
    def __init__(self, variant):
        self.cell, self.win = None, False
        self.logger = Logger(variant)

    def make_move(self):
        side = self.logger.get_move()
        if self.cell.is_exit(side):
            self.win = True
            return
        if not self.cell.can_go(side):
            self.logger.send_message("Стенка")
        else:
            self.logger.send_message("Успешно")
            self.cell = self.cell.get_neighbour(side)
        self.cell = self.cell.apply_effects(self.logger)
