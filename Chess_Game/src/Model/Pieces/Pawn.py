from Model.Piece import Piece, PieceColor, PieceType



class Pawn(Piece):

    def __init__(self, isWhite):
        Piece.__init__(self,isWhite, PieceType.Pawn)
        self.type = PieceType.Pawn
        
        

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
            print("This pawn has already moved and can now only move one space forward at a time.")
            return False
        
        if diffRow != 1 and diffRow != 2:
            print("That is too far for a pawn to move in Y.")
            return False
        
        if diffCol != 0:
            destOcc = destination.getIsOccupied()
            
            if destOcc == False:
                print("You can't capture an empty space.")
                return False
            
            # this method needs to be implemented as a java equivalent
            # if destination.getPiece().getPieceColor().compareTo(this.getPieceColor()) == 0
            #       System.out.println("You can't capture your allies.");
			#       return false;
        
            return True
        
        
        if destination.getIsOccupied == True:
            print("Pawns cannot interact with pieces directly ahead")
            return False
        
        return True
    