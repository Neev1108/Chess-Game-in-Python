
from Model.Tile import Tile
from abc import ABC, abstractmethod

class PieceType(ABC):
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
    currenTile = ""
    hasMoved = False
    colorString = ""
    
    def __init__(self, isWhite, type):
        self.isWhite = isWhite
        if isWhite == True:
            self.color = PieceColor.White
            self.colorString = "White"
        else:
            self.color = PieceColor.Black
            self.colorString = "Black"
        self.type = type
        

    def isWhite(self):
        return self.isWhite
    
    def getPieceColor(self):
        return self.color
    
    def getPieceType(self):
        return self.type
    
    def setCurrentTile(self, newTile: Tile):
        self.currentTile = newTile
        
    def getCurrentTile(self) -> Tile:
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
    
    def getColorString(self, isWhite):
        if isWhite == True:
            return "White"
        else:
            return "Black"
        
        
    def __str__(self):
        return self.getColorString() + " " + self.getPieceType()
    
    
    @abstractmethod
    def isValidMove(self, origin: Tile, destination:Tile) -> bool:
        pass
    
     
    def move(self, origin: Tile, destination:Tile):
        destination.setPiece(origin.getPiece())
        origin.setPiece(None)
        destination.setOccupied(True)
        origin.setOccupied(False)
        self.setHasMoved(True)
            
          
    
    