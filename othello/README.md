Desktop Othello app using Python and Processing. Player plays against computer. 

How the ai works: 
Scans the board from the upper left corner on down for legal moves. Makes the first 
legal move it finds. 

In the method player_can_play, when a user clicks on an empty piece, it looks at 
the 8 neighbor pieces around it. For each one, if it is the opposite color, it 
keeps moving in that direction until it hits a piece with the same color. Then it 
flips the surrounding pieces and moves on to the next of the 8 neighbors.


