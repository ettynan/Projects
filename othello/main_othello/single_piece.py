class SinglePiece():

    BLACK = 0
    WHITE = 1

    def __init__(self, x, y):
        self.SIZE = 50
        self.x = x
        self.y = y
        self.color = None

    def flip(self):
        if(not self.isEmpty()):
            new_color = (self.color + 1) % 2
            self.display(new_color)

    def place_piece(self, player):
        """If piece already places, returns false"""
        if(self.isEmpty()):
            self.display(player)
            return True
        else:
            return False

    def display(self, player):
        """Draw circular piece to screen"""
        noStroke()
        self.color = player
        fill(self.color)
        ellipse(self.x, self.y, self.SIZE, self.SIZE)

    def isEmpty(self):
        """Returns none for self.color"""
        return self.color is None
