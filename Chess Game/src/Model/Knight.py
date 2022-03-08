import Piece
import Tile
from Piece import PieceType, PieceColor


class Knight(Piece):
    type = PieceType()

    def __init__(self, isWhite):
        super(isWhite, PieceType.Knight)

    def getType(self):
        return self.type

    def isValidMove(origin: Tile, destination: Tile):

        if destination.getIsOccupied() == True:
            if destination.getPiece().isWhite() == self.isWhite():
                return False

        x_diff = abs(destination.getRow() - origin.getRow())
        y_diff = abs(destination.getCol() - origin.getCol())

        if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
            return True
        
        
        return False
