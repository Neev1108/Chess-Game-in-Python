
from Model.Tile import Tile
from Model.Piece import Piece, PieceColor, PieceType


class Knight(Piece):

    def __init__(self, isWhite):
        Piece.__init__(self,isWhite, PieceType.Knight)
        self.type = PieceType.Knight

    def getType(self):
        return self.type
    
    def getColorString(self):
        return super().getColorString(self.isWhite)
    

    def isValidMove(self, origin: Tile, destination: Tile):

        if destination.getIsOccupied() == True:
            if destination.getPiece().isWhite() == self.isWhite:
                return False

        x_diff = abs(destination.getRow() - origin.getRow())
        y_diff = abs(destination.getCol() - origin.getCol())

        if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
            return True
        
        
        return False
