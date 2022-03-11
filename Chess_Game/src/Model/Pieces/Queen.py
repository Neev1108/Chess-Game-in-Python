from Model.Piece import Piece, PieceColor, PieceType
from Model.Tile import Tile


class Queen(Piece):

    def __init__(self, isWhite):
        super().__init__(isWhite, PieceType.Queen)
        self.type = PieceType.Queen
        
    def getType(self):
        return self.type

    def isValidMove(start: Tile, end: Tile):
        x_diff = abs(end.getRow() - start.getRow())
        y_diff = abs(end.getCol() - start.getCol())

        print("x diff: " + x_diff + "     y diff: " + y_diff)

        if x_diff == y_diff or end.getRow() == start.getRow() or end.getCol() == start.getCol():
            return True

        return False
        
