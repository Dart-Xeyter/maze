import argparse
from config import max_number

parser = argparse.ArgumentParser()
parser.add_argument('side_length', type=int, choices=range(2, max_number+1),
                    help=f'длина стороны лабиринта от 2 до {max_number}')
parser.add_argument('--easy', action='store_true', dest='show_field')
parser.add_argument('-p', type=int, default=1, dest='num_players',
                    choices=range(1, max_number+1), help=f'число игроков от 1 до {max_number}')
parser.add_argument('-r', type=int, dest='river_max_len',
                    choices=range(2, max_number**2+1), help='длина реки (хотя бы 2)')
parser.add_argument('-t', type=int, dest='tunnel_max_len',
                    choices=range(1, max_number**2+1), help='длина туннеля (хотя бы 1)')
parser.add_argument('-w', type=int, dest='walls_max_num', help='количество стенок')
parser.add_argument('-g', '--debug', action='store_true', help=argparse.SUPPRESS)
arguments = parser.parse_args()
