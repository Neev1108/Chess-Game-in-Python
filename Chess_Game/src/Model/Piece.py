
from Model.Tile import Tile

class PieceType():
    King = "K"
    Queen = "Q"
    Knight = "C"
    Bishop = "B"
    Pawn = "P"
    Rook = "R"
    
class PieceColor():
    White = "W"
    Black = "B"

class Piece():
    
    isWhite = False
    color = ""
    PieceAlive = True
    hasMoved = False
    colorString = ""
    currenTile = ""
    hasMoved = False
    
    def __init__(self, isWhite, type):
        self.isWhite = isWhite
        if isWhite == True:
            self.color = PieceColor.White
        else:
            self.color = PieceColor.Black
        self.type = type
        

    def isWhite(self):
        return self.isWhite
    
    def getPieceColor(self):
        return self.color
    
    def getPieceType(self):
        return self.type
    
    def setCurrentTile(self, newTile: Tile):
        self.currentTile = newTile
        
    def getCurrentTile(self):
        return self.currentTile
    
    def getPieceType(self):
        return self.type
    
    def pieceDied(self):
        self.PieceAlive = False
        return self.PieceAlive
    
    
    def getHasMoved(self):
        return self.hasMoved
    
    def setHasMoved(self, b: bool):
        self.hasMoved = b
        
    def getColorString(self):
        return self.colorString
        
    def __str__(self):
        return self.getColorString + " " + self.getPieceType()
    
     
    def move(self, origin: Tile, destination:Tile):
        destination.setPiece(origin.getPiece())
        origin.setPiece(None)
        destination.setIsOccupied(True)
        origin.setIsOccupied(False)
        self.setHasMoved(True)
            
          
    
    