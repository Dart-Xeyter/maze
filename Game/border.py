class Border:
    def __init__(self, can_go, is_exit):
        self.can_go = can_go
        self.is_exit = is_exit

    def __str__(self):
        return ' ' if self.can_go else '#'

    def __repr__(self):
        return str(self)
