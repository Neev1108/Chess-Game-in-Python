
import Piece
import Tile
from Piece import PieceType, PieceColor


class King(Piece):
    type = PieceType()
    isInCheck = bool(False)


    def __init__(self, isWhite):
        super(isWhite, PieceType.King)
        
    def getType(self):
        return self.type

    def setInCheck(self, inCheck):
        self.inCheck = inCheck

    def getIsInCheck(self):
        return self.isInCheck

    def isValidMove(start: Tile, end: Tile):
        diffRow = start.getRow() - end.getRow()
        diffRow = abs(diffRow)
        diffCol = start.getCol() - end.getCol()
        diffCol = abs(diffCol)

        if diffRow > 1 or diffCol > 1:
            return False
        
        return True

       
    #    Need to implement this in python using comparision operator overloading
    #    __eq__ is how it works
       
    #    if (end.getIsOccupied() == true)
    # 	{
    # 		if (end.getPiece().getColorString().compareTo(start.getPiece().getColorString()) == 0)
    # 		{
    # 			System.out.println("That tile is already held by an ally");
    # 			return false;
    # 		}
    # 	}

       
       

            
        
    
    
