from Model.Tile import Tile
from Model.Piece import Piece, PieceColor, PieceType

class Rook(Piece):
    
    def __init__(self, isWhite):
        super().__init__(isWhite, PieceType.Rook)
        self.type = PieceType.Rook
        
    def getType(self):
        return self.type
    
    def isValidMove(start: Tile, end: Tile):
        if end.getRow() == start.getRow() or end.getCol() == start.getCol():
            return True

        return False