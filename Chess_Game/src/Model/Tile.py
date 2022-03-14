
 
class Tile:
    
    
    def __init__(self, row, col, piece):
        self.occupied = False
        self.piece = piece
        self.row = row
        self.col = col
        
        if piece == None:
            self.occupied = False
        else:
            self.occupied = True
            
        
    def getPiece(self):
        return self.piece
    
    def setPiece(self, piece):
        self.piece = piece
        
    def getRow(self):
        return self.row
    
    def setRow(self, row):
        self.row = row
        
    def getCol(self):
        return self.col
    
    def setCol(self, col):
        self.col = col
        
    def getOccupied(self):
        return self.occupied
    
    def setOccupied(self, occupied: bool):
        self.occupied = occupied
        
    def __str__(self):
        return str((self.row, self.col))