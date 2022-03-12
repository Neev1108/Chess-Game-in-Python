from Model.Board import Board
from Model.Player import Player
from Model.Moves import Moves
from Model.Piece import Piece
from Model.Pieces.King import King


class GameEvent():
    WHITE_WIN = "1"
    BLACK_WIN = "2"
    IN_PROGRESS = "3"
    PAUSED = "4"
    NOT_STARTED = "5"


class Model:
    def __init__(self):
        self.board = Board().getBoard()
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
        b = self.board
        for x in range(8):
            for y in range(8):
                if b[x][y].getPiece() == None:
                    print("-  ", end="")
                    if y == 7:
                        print()
                else:
                    print(str(b[x][y].getPiece().getPieceColor()) +
                          str(b[x][y].getPiece().getPieceType()) + " ", end=" ")

                    if y == 7:
                        print()
                        
                        
                        

    def playGame(self):
        currentPlayer = self.getPlayer1()

        while self.getEvent != GameEvent.WHITE_WIN and self.getEvent != GameEvent.BLACK_WIN:
            self.printBoard()

            print(currentPlayer.getColor() + " team is making their move.")
            print(
                "Please input the row of the current location of the piece you wish to move:")
            row = int(input())
            

            if row < 0 or row > 7:
                print("That is not a valid coordinate. Please try again.")
                continue

            print(
                "Please input the column of the current location of the piece you wish to move:")
            col = int(input())

            if col < 0 or col > 7:
                print("That is not a valid coordinate. Please try again.")

            currentTile = self.board[row][col]

            if currentTile.getOccupied() == False:
                print("The tile you picked has no piece. Please try again.")
                continue

            currentPiece = currentTile.getPiece()
            if currentPlayer.getColor() != currentPiece.getColorString():
                print("The piece you selected is your opponent's. Please select a " +
                      currentPlayer.getColor() + " piece.")
                continue

            print("You have selected " + currentPiece.getPieceColor() +
                  " " + currentPiece.getPieceType() + ".")

            print(
                "Please input the row of the destination of the piece you wish to move:")
            row = int(input())

            if row < 0 or row > 7:
                print("That is not a valid coordinate. Please try again.")
                continue

            print(
                "Please input the column of the destination location of the piece you wish to move:")
            col = int(input())

            if col < 0 or col > 7:
                print("That is not a valid coordinate. Please try again.")

            targetTile = self.board[row][col]

            currentMove = Moves(currentPlayer, currentTile, targetTile)
            validMove = self.startTurn(currentMove)
            
            if not validMove:
                continue
            print("Move Successful")

            if self.getEvent == GameEvent.BlackWin or self.getEvent == GameEvent.WhiteWin:
                print("Game Over")
                break
            else:
                if self.currentPlayer == self.getPlayer1():
                    self.currentPlayer = self.getPlayer2()

                else:
                    self.currentPlayer = self.getPlayer1()

                print("Turn Complete , " + currentPlayer.toString() +
                      " will begin their turn.")
                
                
                
                
    # Multiple cases for this
    # 1. Not Moving your own piece (not the same color as the player)
    # 2. Checking to make sure that specific piece can make that move
    # 3. Check the destination to see if it falls on an ally piece OR if not knight, then if it collides with an ally
    # 4. Check if the destination is an enemy piece (then delete and such)
    # 5. Check if collision with enemy piece happens (if not Knight of course)
    # 6. King stuff like check, checkmate etc.
    
    
    def startTurn(self, move: Moves) -> bool:

        player = move.getPlayer()
        pieceMoved = move.getPieceMoved()
        endPiece = move.getDestinationPiece()
        print(pieceMoved)
        
        # Number 1 Check
        if player.getColor() != pieceMoved.getColorString():
            print("The piece you selected is your opponent's. Please select a " + player.getColor() + " piece.")
            return False
        
        # Check number 2 and destination checks for ally or enemy (with no collision checks)
        if not pieceMoved.isValidMove(move.getCurrentPos(), move.getEndPos()):
            print("Error: Invalid move.")
            return False
        
            
        if self.checkCollision(move, player, pieceMoved):
            return False
        
        
        if self.checkDestinationForAlly(move, player, pieceMoved):
            return False
        
        
        # Following is King is checks (need to be tweaked)
        
        testAllyKingCheck = False
        
        if player.getColor() == "White":
            testAllyKingCheck = self.kingInCheck(self.board.getWhiteKing())
        else:
            testAllyKingCheck = self.kingInCheck(self.board.getBlackKing())
 
 
        if testAllyKingCheck:
            print("This move would leave your King in danger and thus cannot be performed")
            return False
        
        pieceMoved.move(move.getCurrentPos(), move.endPos)
        
        
        if endPiece != None:
            endPiece.pieceDied()
            
        move.getEndPos().setPiece(move.getPieceMoved())
        move.getCurrentPos().setPiece(None)
        
        print("Move successful")
        
        if endPiece.isinstance(King):
            self.event = GameEvent.WHITE_WIN
            
        else:
            self.event = GameEvent.BLACK_WIN
            
        # if game complete
        if self.getEvent() == GameEvent.BLACK_WIN or self.getEvent == GameEvent.WHITE_WIN:
            print("Game Complete")
            return True
        else:
            #otherwise swap players
            if player == self.getPlayer1():
                player = self.getPlayer2
                
            else:
                player = self.getPlayer1
                
            print("Turn complete, " + str(player) + " will begin their turn.")
        
        if self.doTurn == self.player1:
            self.doTurn = self.player2
        else:
            self.doTurn = self.player1
            
        return True
                
                
                
    
    #These 3 methods need to be worked on
    
    def checkDestinationForAlly(move: Moves, player: Player, piecedMoved: Piece):
        if move.getEndPos().getOccupied() == False:
            return False
        
        if piecedMoved.getColorString() == move.getDestinationPiece().getColorString():
            return True
        
        return False
               
    def checkCollision(move, player, pieceMoved):
        
        return
    
    
    def kingInCheck(King):
        return
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                
