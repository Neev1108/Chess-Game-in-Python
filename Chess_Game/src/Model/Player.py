

class Player():
    
    
    def __init__(self, color):
        self.opponent = []
        self.color = color
        
    
    def getColor(self):
        return self.color
    
    def setColor(self, s: str):
        self.color = s
        
    def __str__(self):
        return self.color + " Player"
    
    
    def getOpponent(self):
        return self.opponent[0]
    
    def setOpponent(self,p):
        self.opponent.append(p)
    
    