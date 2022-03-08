import Piece, Tile
from Piece import PieceType, PieceColor

class Rook(Piece):
    
    def __init__(self, isWhite):
        super(isWhite, PieceType.Rook)
        
    def getType(self):
        return self.type
    
    def isValidMove(start: Tile, end: Tile):
        if end.getRow() == start.getRow() or end.getCol() == start.getCol():
            return True

        return False