from Model.Tile import Tile
from Model.Piece import Piece, PieceColor, PieceType

class Rook(Piece):
    
    def __init__(self, isWhite):
        Piece.__init__(self,isWhite, PieceType.Rook)
        self.type = PieceType.Rook
        
    def getType(self):
        return self.type
    
    def getColorString(self):
        return super().getColorString(self.isWhite)
    
    def isValidMove(start: Tile, end: Tile):
        if end.getRow() == start.getRow() or end.getCol() == start.getCol():
            return True

        return False
    