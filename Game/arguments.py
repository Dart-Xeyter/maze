class Arguments:
    def __init__(self, argv):
        self.repeat = "--repeat" in argv
        self.show_field = "--easy" in argv
        self.river_max_len = self.tunnel_max_len = self.walls_max_num = None
        if '-r' in argv:
            self.river_max_len = int(argv[argv.index('-r')+1])
        if '-t' in argv:
            self.tunnel_max_len = int(argv[argv.index('-t')+1])
        if '-w' in argv:
            self.walls_max_num = int(argv[argv.index('-w')+1])
