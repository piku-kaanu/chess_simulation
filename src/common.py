"""This file contains common utilities."""


class UnsupportedChessPiece(Exception):
    pass


class UnsupportedChessCell(Exception):
    pass


def print_star(count):
    print('*' * count)
