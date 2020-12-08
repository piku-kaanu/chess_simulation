"""This module contains the Piece class which represents a piece in a chessboard and simulates it's move."""

from src import common


class Piece:
    pieces = {'King': {'move': 1},
              'Queen': {'move': 8},
              'Bishop': {'move': 8, 'direction': ['C']},
              'Horse': {'move': 2.5, 'direction': ['V', 'H']},
              'Rook': {'move': 8, 'direction': ['V', 'H']},
              'Pawn': {'move': 1, 'direction': ['V']}}

    def __init__(self, type_, x_position, y_position):
        if type_ not in self.pieces:
            raise common.UnsupportedChessPiece(
                f'Error: Unsupported chess piece type: {type_}\n'
                'Supported types are any one of King, Queen, Bishop, Horse, Rook or Pawn.\n')
        if x_position not in 'ABCDEFGH' or y_position not in range(1, 9):
            raise common.UnsupportedChessPiece(
                f'Error: Unsupported chess cell position: {x_position}{y_position}\n'
                'Supported positions are any one from A1 to A8, B1 to B8 ... H1 to H8')
        self.type_ = type_
        self.x_position = x_position
        self.y_position = y_position
        self.step_move = self.pieces.get(type_).get('move')
        self.direction = self.pieces.get(type_).get('direction', ['V', 'H', 'C'])

    def get_possible_moves(self):
        possible_moves = []

        for direction in self.direction:
            if direction == 'V':
                print('Moves vertical')
            elif direction == 'H':
                print('Moves horizontal')
            elif direction == 'C':
                print('Moves cross ways')

        return ', '.join(possible_moves)
