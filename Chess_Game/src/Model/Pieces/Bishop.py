from Model.Piece import Piece, PieceColor, PieceType
from Model.Tile import Tile

class Bishop(Piece):
    
    
    def __init__(self, isWhite: bool):
        Piece.__init__(self,isWhite, PieceType.Bishop)
        self.type = PieceType.Bishop
        
    
    def getType(self):
        return self.type
    
    
    
    def isValidMove(start: Tile, end: Tile):
        x_diff = abs(end.getRow() - start.getRow())
        y_diff = abs(end.getCol() - start.getCol())
        
        return x_diff == y_diff
        
        