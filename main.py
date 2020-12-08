"""This is the entrypoint file from where simulation will get started!!!"""

from src import piece, common


def take_input_and_validate():
    """This method will take input and validates it.

    :returns
        tuple: bool, failure message if fails/piece.Piece object if succeeds.
    """
    print('Chess piece types: King, Queen, Bishop, Horse, Rook or Pawn.')
    print('Chess Piece position on board: A1 to H8')
    user_in = input('Please enter piece type and position (i.e. King A1): ')
    try:
        piece_type, position = user_in.split()
        x_position, y_position = tuple(position)
        piece_obj = piece.Piece(piece_type, x_position, int(y_position))
        return True, piece_obj
    # TODO: Need to prepare proper error message!
    except common.UnsupportedChessPiece as e:
        return False, e
    except Exception as e:
        return False, 'Value should be in proper format!'


def main():
    common.print_star(100)
    print('Welcome to chess simulation!'.center(100))
    common.print_star(100)
    while True:
        result, obj = take_input_and_validate()
        if not result:
            print(obj)
            break
        possible_moves = obj.get_possible_moves()
        print(possible_moves)


if __name__ == '__main__':
    main()
