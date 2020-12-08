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
        self.x_position = ord(x_position)
        self.y_position = y_position
        self.step_move = self.pieces.get(type_).get('move')
        self.direction = self.pieces.get(type_).get('direction', ['V', 'H', 'C'])

    def get_possible_moves(self):
        possible_moves = []

        min_y = self.y_position - self.step_move
        max_y = self.y_position + self.step_move
        min_y = min_y if min_y >= 1 else 1
        max_y = max_y if max_y <= 8 else 8
        min_x = self.x_position - self.step_move
        max_x = self.x_position + self.step_move
        min_x = min_x if min_x >= 65 else 65
        max_x = max_x if max_x <= 72 else 72

        for direction in self.direction:
            if direction == 'V':
                print('Moves vertical')
                possible_moves.extend(self.__get_range(self.x_position, self.x_position, min_y, max_y))
            elif direction == 'H':
                print('Moves horizontal')
                possible_moves.extend(self.__get_range(min_x, max_x, self.y_position, self.y_position))
            elif direction == 'C':
                print('Moves cross ways')
                possible_moves.extend(self.__get_range(min_x, max_x, min_y, max_y))

        return ', '.join(possible_moves)

    def __get_range(self, min_x, max_x, min_y, max_y, is_cross=False):
        if not is_cross:
            return [chr(i) + str(j) for i in range(min_x, max_x + 1) for j in range(min_y, max_y + 1) if
                    self.x_position != i or self.y_position != j]
        else:
            pass
            # ret_list = []
            # while True:
            #
            # return  ret_list
