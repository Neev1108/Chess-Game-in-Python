
from Model.Tile import Tile
from Model.Piece import Piece
from Model.Player import Player

class Moves:
    
    
    def __init__(self, player: Player, currentPos: Tile, endPos: Tile):
        self.player = player
        self.currentPos = currentPos
        self.endPos = endPos
        
        self.pieceMoved = currentPos.getPiece()
        self.destinationPiece = endPos.getPiece()
        
    
    def getEndPos(self) -> Tile:
        return self.endPos
    
    def getPlayer(self) -> Player:
        return self.player
    
    def getPieceMoved(self) -> Piece:
        return self.pieceMoved
    
    def getCurrentPos(self) -> Tile:
        return self.currentPos
    
    def getDestinationPiece(self) -> Piece:
        return self.destinationPiece
    
    
    
