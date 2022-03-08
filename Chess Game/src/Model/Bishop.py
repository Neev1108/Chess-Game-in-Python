from Piece import PieceType
import Piece
import Tile

class Bishop(Piece):
    
    type = PieceType()
    
    def __init__(self, isWhite: bool):
        super(isWhite, PieceType.Bishop)
        
    
    def getType(self):
        return self.type
    
    
    def isValidMove(start: Tile, end: Tile):
        x_diff = abs(end.getRow() - start.getRow())
        y_diff = abs(end.getCol() - start.getCol())
        
        return x_diff == y_diff
        
        