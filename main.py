"""This is the entrypoint file from where simulation will get started!!!"""

from src import piece, common


def take_input_and_validate():
    """This method will take input and validates it.

    :returns
        tuple: bool, failure message if fails/piece.Piece object if succeeds.
    """
    print('Chess piece types: King, Queen, Bishop, Horse, Rook or Pawn.')
    print('Chess Piece position on board: A1 to A8, B1 to B8 ... H1 to H8.')
    print('Hit enter without input to exit the game.')
    user_in = input('Please enter piece type and position (i.e. King A1): ')
    if not user_in:
        print('Exiting the game!!!\nBye!!!')
        exit()
    try:
        piece_type, position = user_in.split()
        x_position, y_position = tuple(position)
        piece_obj = piece.Piece(piece_type, ord(x_position), int(y_position))
        return True, piece_obj
    # TODO: Need to prepare proper error message!
    except (common.UnsupportedChessPiece, common.UnsupportedChessCell) as e:
        return False, e
    except Exception as e:
        return False, 'Value should be in proper format!'


def main():
    common.print_star(150)
    print('Welcome to chess simulation!'.center(150))
    common.print_star(150)
    while True:
        result, obj = take_input_and_validate()
        if not result:
            common.print_star(150)
            print(obj)
            print('Try Again!')
            common.print_star(150)
            input('Press enter to continue')
            common.print_star(150)
            continue
        possible_moves = obj.get_possible_moves() if obj.type_ != 'Horse' else obj.get_horse_moves()
        print(', '.join(possible_moves))
        common.print_star(150)
        input('Press enter to continue')
        common.print_star(150)


if __name__ == '__main__':
    main()
