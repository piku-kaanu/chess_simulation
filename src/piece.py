"""This module contains the Piece class which represents a piece in a chessboard and simulates it's move."""

from src import common


class Piece:
    pieces = {'King': {'move': common.ONE_MOVE},
              'Queen': {'move': common.FULL_MOVE},
              'Bishop': {'move': common.FULL_MOVE, 'direction': [common.CROSS]},
              'Horse': {'move': common.HORSE_MOVE, 'direction': [common.VERTICAL, common.HORIZONTAL]},
              'Rook': {'move': common.FULL_MOVE, 'direction': [common.VERTICAL, common.HORIZONTAL]},
              'Pawn': {'move': common.ONE_MOVE, 'direction': [common.VERTICAL]}}

    def __init__(self, type_, x_position, y_position):
        if type_ not in self.pieces:
            raise common.UnsupportedChessPiece(
                f'Error: Unsupported chess piece type: {type_}\n'
                'Supported types are any one of King, Queen, Bishop, Horse, Rook or Pawn.\n')
        if x_position not in range(common.MIN_X, common.MAX_X + 1) or \
                y_position not in range(common.MIN_Y, common.MAX_Y + 1):
            raise common.UnsupportedChessCell(
                f'Error: Unsupported chess cell position: {chr(x_position)}{y_position}\n'
                'Supported positions are any one from A1 to A8, B1 to B8 ... H1 to H8')

        self.type_ = type_
        self.x_position = x_position
        self.y_position = y_position
        self.step_move = self.pieces.get(type_).get('move')
        self.direction = self.pieces.get(type_).get('direction', common.ALL_DIRECTIONS)

    def get_possible_moves(self):
        possible_moves = []

        min_y = max(self.y_position - self.step_move, common.MIN_Y)
        max_y = min(self.y_position + self.step_move, common.MAX_Y)
        min_x = max(self.x_position - self.step_move, common.MIN_X)
        max_x = min(self.x_position + self.step_move, common.MAX_X)

        for direction in self.direction:
            if direction == common.VERTICAL:
                if common.IS_DEBUG:
                    print('Moves vertical')
                possible_moves.extend(self.__get_range(self.x_position, self.x_position, min_y, max_y))
            elif direction == common.HORIZONTAL:
                if common.IS_DEBUG:
                    print('Moves horizontal')
                possible_moves.extend(self.__get_range(min_x, max_x, self.y_position, self.y_position))
            elif direction == common.CROSS:
                if common.IS_DEBUG:
                    print('Moves cross ways')
                possible_moves.extend(self.__get_range(min_x, max_x, min_y, max_y, is_cross=True))

        return possible_moves

    def __get_range(self, min_x, max_x, min_y, max_y, is_cross=False):
        if not is_cross:
            return [chr(i) + str(j) for i in range(min_x, max_x + 1) for j in range(min_y, max_y + 1) if
                    self.x_position != i or self.y_position != j]
        else:
            pass
            ret_list = []
            i = 1
            while True:
                count = 0
                if self.x_position - i >= min_x:
                    if self.y_position - i >= min_y:
                        ret_list.append(chr(self.x_position - i) + str(self.y_position - i))
                        count += 1
                    if self.y_position + i <= max_y:
                        ret_list.append(chr(self.x_position - i) + str(self.y_position + i))
                        count += 1
                if self.x_position + i <= max_x:
                    if self.y_position - i >= min_y:
                        ret_list.append(chr(self.x_position + i) + str(self.y_position - i))
                        count += 1
                    if self.y_position + i <= max_y:
                        ret_list.append(chr(self.x_position + i) + str(self.y_position + i))
                        count += 1
                if count == 0:
                    break
                i += 1
            return ret_list

    def get_horse_moves(self):
        possible_moves = []

        if self.x_position + 2 <= common.MAX_X:
            if self.y_position - 1 >= common.MIN_Y:
                possible_moves.append(chr(self.x_position + 2) + str(self.y_position - 1))
            if self.y_position + 1 <= common.MAX_Y:
                possible_moves.append(chr(self.x_position + 2) + str(self.y_position + 1))
        if self.x_position - 2 >= common.MIN_X:
            if self.y_position - 1 >= common.MIN_Y:
                possible_moves.append(chr(self.x_position - 2) + str(self.y_position - 1))
            if self.y_position + 1 <= common.MAX_Y:
                possible_moves.append(chr(self.x_position - 2) + str(self.y_position + 1))
        if self.y_position + 2 <= common.MAX_Y:
            if self.x_position - 1 >= common.MIN_X:
                possible_moves.append(chr(self.x_position - 1) + str(self.y_position + 2))
            if self.x_position + 1 <= common.MAX_X:
                possible_moves.append(chr(self.x_position + 1) + str(self.y_position + 2))
        if self.y_position - 2 >= common.MIN_Y:
            if self.x_position - 1 >= common.MIN_X:
                possible_moves.append(chr(self.x_position - 1) + str(self.y_position - 2))
            if self.x_position + 1 <= common.MAX_X:
                possible_moves.append(chr(self.x_position + 1) + str(self.y_position - 2))

        return possible_moves
