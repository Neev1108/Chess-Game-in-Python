import Board, Player
from enum import Enum

class GameEvent(Enum):
    WhiteWin = "WW"
    BlackWin = "BW"

class Model:
    
    board = Board()
    player1 = Player("White")
    player2 = Player("Black")
    
    doTurn = Player()
    
    event = GameEvent()
    
    def __init__(self):
        if self.player1.getColor() == "White":
            self.doTurn = self.player1
        else:
            self.doTurn = self.player2
            
    
    def getPlayer1(self):
        return self.player1
    
    def getPlayer2(self):
        return self.player2
    
    def getDoTurn(self):
        return self.doTurn
    
    def getEvent(self):
        return self.event
    
    def printBoard(self):
        b = self.board.getBoard()
        
        for x in range(8):
            for y in range(8):
                if b[x][y].getPiece() == None:
                    print("-  ")
                    if y == 7:
                        print(end=" ")
                else:
                    print(b[x][y].getPiece().getPieceColor().toString() + b[x][y].getPiece().getPieceType().toString() + " ")
                    
                    if y == 7:
                        print(end=" ")
                        
    def playGame(self):
        currentPlayer = self.getPlayer1()
        
        while self.getEvent != GameEvent.WhiteWin and self.getEvent != GameEvent.BlackWin:
            self.printBoard()
            
            print(currentPlayer.getColor() + " team is making their move.")
            print("Please input the row of the current location of the piece you wish to move:")
            row = input()
            
            if row < 0 or row > 7:
                print("That is not a valid coordinate. Please try again.")
                continue
            
            print("Please input the column of the current location of the piece you wish to move:")
            col = input()
            
            if col < 0 or col > 7:
                print("That is not a valid coordinate. Please try again.")
                
            currentTile = self.board.getTile(row, col)
            
            if currentTile.getIsOccupied() == False:
                print("The tile you picked has no piece. Please try again.")
                continue
            
            currentPiece = currentTile.getPiece()
            if currentPlayer.getColor() == currentPiece.getColorString():
                print("The piece you selected is your opponent's. Please select a " + currentPlayer.getColor() + " piece.")
                continue
            
            print("You have selected " + currentPiece.getPieceColor() + " " + currentPiece.getPieceType() + ".")
            
    
    
            print("Please input the row of the destination of the piece you wish to move:")
            row = input()
            
            if row < 0 or row > 7:
                print("That is not a valid coordinate. Please try again.")
                continue
            
            print("Please input the column of the destination location of the piece you wish to move:")
            col = input()
            
            if col < 0 or col > 7:
                print("That is not a valid coordinate. Please try again.")
                
            
            targetTile = self.board.getTile(row, col)
            
            # Need to work on this
            
            # Moves currentMove = new Moves(currentPlayer, currentTile, targetTile);
			# boolean validMove = this.startTurn(currentMove);
			# if (!validMove)
			# 	continue;
			# System.out.println("Move successful\n");
   
   
            if self.getEvent == GameEvent.BlackWin or self.getEvent == GameEvent.WhiteWin:
                print("Game Over")
                break
            else:
                if self.currentPlayer == self.getPlayer1():
                    self.currentPlayer = self.getPlayer2()
                    
                else:
                    self.currentPlayer = self.getPlayer1()
                    
                print("Turn Complete , " + currentPlayer.toString() + " will begin their turn.")
                
    
