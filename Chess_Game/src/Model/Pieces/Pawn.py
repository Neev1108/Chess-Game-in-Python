from Model.Piece import Piece, PieceColor, PieceType


class Pawn(Piece):

    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, PieceType.Pawn)
        self.type = PieceType.Pawn

    def getColorString(self):
        return super().getColorString(self.isWhite)

    def getType(self):
        return self.type

    def isValidMove(self, origin, destination):
        diffRow = origin.getRow() - destination.getRow()
        diffCol = origin.getCol() - destination.getCol()

        diffRow = abs(diffRow)
        diffCol = abs(diffCol)

        if diffCol > 1:
            print("That is too far for a pawn to move in X.")
            return False
        if self.getHasMoved() == True and diffRow == 2:
            print(
                "This pawn has already moved and can now only move one space forward at a time.")
            return False

        if diffRow != 1 and diffRow != 2:
            print("That is too far for a pawn to move in Y.")
            return False

        if diffCol != 0:
            destOcc = destination.getOccupied()

            if destOcc == False:
                print("You can't capture an empty space.")
                return False

            if destination.getPiece().getPieceColor()  == destination.getPiece().getPieceColor():
                print("You can't capture your allies.")
                return False

            return True

        if destination.getOccupied == True:
            print("Pawns cannot interact with pieces directly ahead")
            return False

        return True
