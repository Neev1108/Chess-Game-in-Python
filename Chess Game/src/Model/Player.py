

class Player():
    color = str("")
    
    # Need to modify logic on how to store opponent info
    # Python has trouble creating an object in its own class definition
    
    opponent = Player()
    
    def __init__(self, color):
        self.color = color
        
    
    def getColor(self):
        return self.color
    
    def setColor(self, s: str):
        self.color = s
        
    def __str__(self):
        return self.color + " Player"
    
    
    def getOpponent() -> Player:
        return opponent
    
    def setOpponent(p: Player):
        self.opponent = p
    
    