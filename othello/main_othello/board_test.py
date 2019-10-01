from pieces import Pieces
from board import Board


def test_constructor():
    board = Board(600, 8)
    pieces = Pieces(600, 8)

    assert board.BOXES == 8
    assert board.box_size == 75


def test_play():
    pass


def test_no_more_moves():
    pass


def test_determine_winner():
    pass


def test_computer_move():
    pass
