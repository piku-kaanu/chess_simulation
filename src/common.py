"""This file contains common utilities."""

MIN_X = ord('A')
MAX_X = ord('H')
MIN_Y = 1
MAX_Y = 8

VERTICAL = 'v'
HORIZONTAL = 'h'
CROSS = 'c'
ALL_DIRECTIONS = ['v', 'h', 'c']

ONE_MOVE = 1
FULL_MOVE = 8
HORSE_MOVE = 2.5

IS_DEBUG = True


class UnsupportedChessPiece(Exception):
    pass


class UnsupportedChessCell(Exception):
    pass


def print_star(count):
    print('*' * count)
