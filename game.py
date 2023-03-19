import random


class Border:
    def __init__(self, can_go, is_exit):
        self.can_go = can_go
        self.is_exit = is_exit


class Cell:
    def __init__(self, x, y, field):
        self.x, self.y = x, y
        self.field = field

    def get_border(self, side):
        if side % 2 == 1:
            return self.field.columns[self.y][self.x+(side == 3)]
        return self.field.rows[self.x][self.y+(side == 2)]

    def can_go(self, side):
        return self.get_border(side).can_go

    def is_exit(self, side):
        return self.get_border(side).is_exit


class EmptyCell(Cell):
    state = ""

    def apply_effects(self):
        return self


class Field:
    def __init__(self, n):
        self.n = n
        self.field = [[] for _ in range(n)]
        self.rows = [[] for _ in range(n)]
        self.columns = [[] for _ in range(n)]
        for q in range(n):
            for q1 in range(n+1):
                self.rows[q].append(Border(0 < q1 < n, False))
                self.columns[q].append(Border(0 < q1 < n, False))
        exit_border = random.choice([self.rows, self.columns])[random.randint(0, n-1)][random.choice([0, n])]
        exit_border.can_go = exit_border.is_exit = True
        for q in range(n):
            for q1 in range(n):
                self.field[q].append(EmptyCell(q, q1, self))
        # нагенерить стенки внутри

    def __getitem__(self, item):
        return self.field[item]


class Player:
    def __init__(self):
        self.cell = self.win = None

    def get_start(self, n):
        while True:
            try:
                x, y = map(lambda t: int(t)-1, self.get_message().split())
                assert(-1 < min(x, y) and max(x, y) < n)
                return x, y
            except (ValueError, AssertionError):
                self.send_message("Некорректные координаты")

    def get_move(self):
        commands = {'-': 0, 'u': 1, 'r': 2, 'd': 3, 'l': 4}
        while True:
            try:
                return commands[self.get_message()]
            except KeyError:
                self.send_message("Некорректный ход")

    def make_move(self):
        moves = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        q = self.get_move()
        x, y = self.cell.x+moves[q][0], self.cell.y+moves[q][1]
        if q != 0 and self.cell.is_exit(q):
            self.send_message("Поздравляем, вы вышли из лабиринта!")
            self.win = True
            return
        if q != 0 and not self.cell.can_go(q):
            self.send_message("Стенка")
        else:
            self.send_message("Успешно")
            self.cell = self.cell.field[x][y]
        self.send_message(self.cell.state)
        self.cell = self.cell.apply_effects()

    def get_message(self):
        return input()

    def send_message(self, s):
        if s:
            print(s)


class Game:
    def __init__(self, player):
        self.player = player

    def game(self, n):
        field = Field(n)
        x, y = self.player.get_start(n)
        self.player.cell = field[x][y]
        self.player.win = False
        while self.player.win is False:
            self.make_move()

    def make_move(self):
        self.player.make_move()


if __name__ == "__main__":
    game = Game(Player())
    play = True
    while play:
        size = int(input("Введите размер поля: "))
        game.game(size)
        verdict = input("Начать новую игру? ")
        while verdict not in ['y', 'n']:
            verdict = input("Некорректный ответ\n")
        play = (verdict == 'y')

