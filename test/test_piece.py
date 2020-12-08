"""This is going to be the test file"""

import pytest

from src import piece, common


def test_init_positive():
    obj = piece.Piece('King', ord('D'), 5)
    assert obj.type_ == 'King'
    assert obj.x_position == ord('D')
    assert obj.y_position == 5
    assert obj.step_move == common.ONE_MOVE
    assert obj.direction == common.ALL_DIRECTIONS


def test_init_negative_type():
    pytest.raises(common.UnsupportedChessPiece, piece.Piece, 'Random', ord('D'), 5)


def test_init_negative_cell_x():
    pytest.raises(common.UnsupportedChessCell, piece.Piece, 'King', ord('I'), 5)


def test_init_negative_cell_y():
    pytest.raises(common.UnsupportedChessCell, piece.Piece, 'King', ord('D'), 10)


@pytest.mark.parametrize(
    'chess_piece, expected_result',
    [('King', 'D4, D6, C5, E5, C4, C6, E4, E6'),
     ('Queen',
      'D1, D2, D3, D4, D6, D7, D8, A5, B5, C5, E5, F5, G5, H5, C4, C6, E4, E6, B3, B7, F3, F7, A2, A8, G2, G8, H1'),
     ('Bishop', 'C4, C6, E4, E6, B3, B7, F3, F7, A2, A8, G2, G8, H1'),
     ('Rook', 'D1, D2, D3, D4, D6, D7, D8, A5, B5, C5, E5, F5, G5, H5'),
     ('Pawn', 'D4, D6')])
def test_get_possible_moves_piece(chess_piece, expected_result):
    obj = piece.Piece(chess_piece, ord('D'), 5)
    actual_result = obj.get_possible_moves()
    for i in actual_result:
        assert i in expected_result


@pytest.mark.parametrize(
    'chess_piece, expected_result',
    [('King', 'A4, A6, B5, B4, B6'),
     ('Queen', 'A1, A2, A3, A4, A6, A7, A8, B5, C5, D5, E5, F5, G5, H5, B4, B6, C3, C7, D2, D8, E1'),
     ('Bishop', 'B4, B6, C3, C7, D2, D8, E1'),
     ('Rook', 'A1, A2, A3, A4, A6, A7, A8, B5, C5, D5, E5, F5, G5, H5'),
     ('Pawn', 'A4, A6')])
def test_get_possible_moves_piece_edge_vertical(chess_piece, expected_result):
    obj = piece.Piece(chess_piece, ord('A'), 5)
    actual_result = obj.get_possible_moves()
    for i in actual_result:
        assert i in expected_result


@pytest.mark.parametrize(
    'chess_piece, expected_result',
    [('King', 'D2, C1, E1, C2, E2'),
     ('Queen', 'D2, D3, D4, D5, D6, D7, D8, A1, B1, C1, E1, F1, G1, H1, C2, E2, B3, F3, A4, G4, H5'),
     ('Bishop', 'C2, E2, B3, F3, A4, G4, H5'),
     ('Rook', 'D2, D3, D4, D5, D6, D7, D8, A1, B1, C1, E1, F1, G1, H1'),
     ('Pawn', 'D2')])
def test_get_possible_moves_piece_edge_horizontal(chess_piece, expected_result):
    obj = piece.Piece(chess_piece, ord('D'), 1)
    actual_result = obj.get_possible_moves()
    for i in actual_result:
        assert i in expected_result


@pytest.mark.parametrize(
    'chess_piece, expected_result',
    [('King', 'A2, B1, B2'),
     ('Queen', 'A2, A3, A4, A5, A6, A7, A8, B1, C1, D1, E1, F1, G1, H1, B2, C3, D4, E5, F6, G7, H8'),
     ('Bishop', 'B2, C3, D4, E5, F6, G7, H8'),
     ('Rook', 'A2, A3, A4, A5, A6, A7, A8, B1, C1, D1, E1, F1, G1, H1'),
     ('Pawn', 'A2')])
def test_get_possible_moves_piece_corner(chess_piece, expected_result):
    obj = piece.Piece(chess_piece, ord('A'), 1)
    actual_result = obj.get_possible_moves()
    for i in actual_result:
        assert i in expected_result


def test_get_possible_moves_horse():
    obj = piece.Piece('Horse', ord('D'), 5)
    actual_result = obj.get_horse_moves()
    expected_result = 'F4, F6, B4, B6, C7, E7, C3, E3'
    for i in actual_result:
        assert i in expected_result


def test_get_possible_moves_horse_edge_vertical():
    obj = piece.Piece('Horse', ord('A'), 5)
    actual_result = obj.get_horse_moves()
    expected_result = 'C4, C6, B7, B3'
    for i in actual_result:
        assert i in expected_result


def test_get_possible_moves_horse_edge_horizontal():
    obj = piece.Piece('Horse', ord('D'), 1)
    actual_result = obj.get_horse_moves()
    expected_result = 'F2, B2, C3, E3'
    for i in actual_result:
        assert i in expected_result


def test_get_possible_moves_horse_corner():
    obj = piece.Piece('Horse', ord('A'), 1)
    actual_result = obj.get_horse_moves()
    expected_result = 'C2, B3'
    for i in actual_result:
        assert i in expected_result
