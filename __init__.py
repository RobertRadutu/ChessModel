from enum import Enum

PAWN   : int = 1
BISHOP : int = 2
KNIGHT : int = 3
ROOK   : int = 4
KING   : int = 5
QUEEN  : int = 6

class Status(enum.IntFlag):
  VALID = 0
  NO_WHITE_KING = 1 << 0 
  NO_BLACK_KING = 1 << 1
  TOO_MANY_KING = 1 << 2

class Board(object):
  legal_moves : []
  def __init__(self):
    pass
  def __print__(self):
    pass

b = Board()
print(b)
print(Status.TOO_MANY_KING)
