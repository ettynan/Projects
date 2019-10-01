from single_piece import SinglePiece


class Pieces:

    BLACK = 0
    WHITE = 1

    """A class of all of the game pieces"""

    def __init__(self, WIDTH, BOXES):
        self.WIDTH = WIDTH
        self.BOXES = BOXES
        self.box_width = WIDTH / BOXES

        self.all_boxes = []
        for r in range(BOXES):
            row = []
            for c in range(BOXES):
                x = c * self.box_width
                y = r * self.box_width
                piece = SinglePiece(x + self.box_width / 2,
                                    y + self.box_width / 2)
                row.append(piece)
            self.all_boxes.append(row)

    def starting_pieces(self):
        """Displays default initial pieces"""
        half = self.BOXES / 2
        self.all_boxes[half - 1][half - 1].place_piece(self.WHITE)
        self.all_boxes[half - 1][half].place_piece(self.BLACK)
        self.all_boxes[half][half - 1].place_piece(self.BLACK)
        self.all_boxes[half][half].place_piece(self.WHITE)

    def opposite_color(self, color):
        """Returns the opposite color"""
        return (color + 1) % 2

    def player_can_play(self, row, column, player, make_move):
        """Searches for pieces to flip, returns false if none to flip, else
        makes the move"""
        piece = self.all_boxes[row][column]
        flipped = False

        if(piece.isEmpty()):
            # Check all pieces surrounding chosen piece
            for r in range(row - 1, row + 2):
                for c in range(column - 1, column + 2):

                    # Don't look at chosen piece itself
                    if(c != column or r != row):
                        maybe_flip = []
                        deltaX = c - column
                        deltaY = r - row

                        # Get the next piece in that particular direction
                        cur_row = row + deltaY
                        cur_col = column + deltaX
                        next = self.get_piece(cur_row, cur_col)

                        while(next is not None and next.color ==
                              self.opposite_color(player)):
                            maybe_flip.append(next)
                            cur_row = cur_row + deltaY
                            cur_col = cur_col + deltaX
                            next = self.get_piece(cur_row, cur_col)

                        if(next is not None and next.color == player and
                           len(maybe_flip) != 0):
                            if(not make_move):
                                return True
                            piece.place_piece(player)
                            for p in maybe_flip:
                                p.flip()
                            flipped = True

        return flipped

    def play(self, x, y, player):
        """Returns true if valid move"""
        column = x / self.box_width
        row = y / self.box_width
        return self.player_can_play(row, column, player, True)

    def get_piece(self, r, c):
        """Returns a piece for that box"""
        if(self.on_board(r) and self.on_board(c)):
            return self.all_boxes[r][c]
        else:
            return None

    def on_board(self, l):
        """Checks that the space is on the board"""
        return l >= 0 and l < self.BOXES

    def no_more_moves(self, player):
        """Loops through rows and columns to find moves"""
        for r in range(self.BOXES):
            for c in range(self.BOXES):
                if(self.player_can_play(r, c, player, False)):
                    return False
        return True

    def computer_move(self, player):
        """Loops through row and column to find legal computer move"""
        for r in range(self.BOXES):
            for c in range(self.BOXES):
                if(self.player_can_play(r, c, player, True)):
                    return

    def determine_winner(self):
        """Counts black and white pieces in board boxes and returns winner"""
        black = 0
        white = 0

        # Loops through board rows and columns counting pieces of each color
        for r in range(self.BOXES):
            for c in range(self.BOXES):
                if(self.all_boxes[r][c].color == self.BLACK):
                    black += 1
                if(self.all_boxes[r][c].color == self.WHITE):
                    white += 1

        if black == white:
            fill(255, 0, 0)
            message = "Tie!"

        def input(self, message=''):
            from javax.swing import JOptionPane
            return JOptionPane.showInputDialog(frame, message)

        if black > white:
            fill(0, 0, 0)
            message = "Black Wins!"

            answer = input('Enter your name')
            if answer:
                print('hi ' + answer)
                file = open("scores.txt", "r+")
                lines = file.readlines()
                if len(lines) == 0:
                    file.write(answer + " " + str(black) + "\n")
                else:
                    list_scores = lines[0].split(" ")
                    score = int(list_scores[1])
                    print(score)
                    if (black > score):
                        lines.insert(0, answer + " " + str(black) + "\n")
                    else:
                        lines.append(answer + " " + str(black) + "\n")
                    file.seek(0)
                    for line in lines:
                        file.write(line)
                file.close()
                
            elif answer == '':
                print('[empty string]')
            else:
                print(answer)  # Canceled dialog will print None

        if white > black:
            fill(100, 100, 100)
            message = "White Wins!"

        textSize(20)
        text(message + " Black " + str(black) + " to White " + str(white),
             self.WIDTH/2 - 140, self.WIDTH/2)
