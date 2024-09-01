State(Board)
Move = F(State), determine the function through ML


Pawn
Rook
Bishop
Knight
Queen
King
Castle availability
-> 7 values common for White & Black

Blank
En passant
-> 2 values independent of White & Black

=> 7 * 2 + 2 = 16 values, can be represented by 4 bits

Extra state: White or Black moves -> 1 bit

Input to the Deep Learning model: 8 * 8 * 4 + 1 = 257 bits (The full representation of a chess board in a vector of 0 or 1)
