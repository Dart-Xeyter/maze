class Arguments:
    def __init__(self, argv):
        self.repeat = "--repeat" in argv
        self.show_field = "--easy" in argv
        self.num_players = int(argv[argv.index('-p')+1]) if '-p' in argv else 1
        if '-n' in argv:
            self.side_length = int(argv[argv.index('-n')+1])
            assert self.side_length >= 2, "Длина стороны лабиринта должна быть хотя бы 2"
        else:
            raise AttributeError("Вы не указали длину стороны лабиринта")
        self.river_max_len = self.tunnel_max_len = self.walls_max_num = None
        if '-r' in argv:
            self.river_max_len = int(argv[argv.index('-r')+1])
            assert self.river_max_len >= 2, "Длина реки должна быть хотя бы 2"
        if '-t' in argv:
            self.tunnel_max_len = int(argv[argv.index('-t')+1])
            assert self.tunnel_max_len >= 1, "Длина туннеля должна быть хотя бы 1"
        if '-w' in argv:
            self.walls_max_num = int(argv[argv.index('-w')+1])
        self.debug = '-g' in argv
