from pieces import Pieces


class Board:
    """Class displays the game board"""
    def __init__(self, WIDTH, BOXES):
        self.BOXES = BOXES
        self.box_size = WIDTH/self.BOXES
        self.pieces = Pieces(WIDTH, BOXES)

    def set_up_board(self):
        """Place desired number of cells on the board"""
        for i in range(self.BOXES):
            for j in range(self.BOXES):
                x = i * self.box_size
                y = j * self.box_size
                stroke(0)
                fill(0, 0.6, 0)
                rect(x, y, self.box_size, self.box_size)
        self.pieces.starting_pieces()

    def play(self, x, y, player):
        """Returns pieces"""
        return self.pieces.play(x, y, player)

    def no_more_moves(self, player):
        return self.pieces.no_more_moves(player)

    def determine_winner(self):
        self.pieces.determine_winner()

    def computer_move(self, player):
        self.pieces.computer_move(player)
