from pieces import Pieces
from board import Board


class GameController:

    BLACK = 0
    WHITE = 1

    def __init__(self, WIDTH, BOXES):
        self.pieces = Pieces(WIDTH, BOXES)
        self.board = Board(WIDTH, BOXES)
        self.player = self.BLACK

    def click(self, mouseX, mouseY):
        """On mouse click starts the game"""
        valid = self.board.play(mouseX, mouseY, self.player)
        if(valid):
            self.change_players()

    def change_players(self):
        """Switches players for alternating turns"""
        self.player = (self.player + 1) % 2
        if(self.board.no_more_moves(self.player)):
            self.player = (self.player + 1) % 2
        if(self.board.no_more_moves(self.player)):
            self.game_over()
            return

    def set_up_game(self):
        """Method that sets up the board"""
        self.board.set_up_board()

    def computer_move(self):
        """Method for computer's move"""
        self.board.computer_move(self.player)
        self.change_players()

    """Gives score after the squares are filled"""
    def game_over(self):
        self.board.determine_winner()
