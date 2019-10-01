from board import Board
from pieces import Pieces
from game_controller import GameController

WIDTH = 600
BOXES = 8
DELAY = 30

game_controller = GameController(WIDTH, BOXES)


def setup():
    """Size of the board"""
    size(WIDTH, WIDTH)
    colorMode(RGB, 1)
    background(0.0, 0.6, 0.0)
    game_controller.set_up_game()


def draw():
    global DELAY
    if(game_controller.player == game_controller.WHITE):
        DELAY -= 1
        if DELAY == 0:
            game_controller.computer_move()
            DELAY = 30


def mousePressed():
    game_controller.click(mouseX, mouseY)
