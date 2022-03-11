from Model.Board import Board
from Model.Player import Player

class GameEvent():
    WhiteWin = "1"
    BlackWin = "2"
    IN_PROGRESS = "3"
    PAUSED = "4"
    NOT_STARTED = "5"
    
class Model:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("White")
        self.player2 = Player("Black")
    
        self.doTurn = self.player1
        self.event = GameEvent.NOT_STARTED
        
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
                    print("-  ", end="")
                    if y == 7:
                        print()
                else:
                    print(str(b[x][y].getPiece().getPieceColor()) + str(b[x][y].getPiece().getPieceType()) + " ", end =" ")
                    
                    if y == 7:
                        print()
                        
                        
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
                
                        
                  
                  