from single_piece import SinglePiece
from pieces import Pieces

BLACK = 0
WHITE = 1


def test_constructor():
    pieces = Pieces(600, 8)
    single_piece = SinglePiece

    assert pieces.WIDTH == 600
    assert pieces.BOXES == 8
    assert pieces.box_width == 75


def test_opposite_color():
    assert (BLACK + 1) % 2 == 1
    assert (WHITE + 1) % 2 == 0


def test_player_can_play():
    pass


def test_play():
    pass


def test_get_pieces():
    pass


def test_on_board():
    pass


def test_no_more_moves():
    pass


def test_computer_move():
    pass


def test_determine_winner():
    pass
