from Model.Board import Board
from Model.Player import Player
from Model.Moves import Moves
from Model.Tile import Tile
from Model.Piece import Piece, PieceType
from Model.Pieces.King import King


class GameEvent:
    WHITE_WIN = "1"
    BLACK_WIN = "2"
    IN_PROGRESS = "3"
    PAUSED = "4"
    NOT_STARTED = "5"


class Model:
    
    # Constructor for the Model
    def __init__(self):
        self.board = Board().getBoard()
        self.player1 = Player("White")
        self.player2 = Player("Black")

        self.doTurn = self.player1
        self.event = GameEvent.NOT_STARTED

        # Checking if the color of the first moving player is white.
        if self.player1.getColor() == "White":
            self.doTurn = self.player1
        else:
            self.doTurn = self.player2

    """
	 Method to get the Player1
	 @return player
    """
    def getPlayer1(self):
        return self.player1


    """
    /**
	 * Method to get the Player
	 * @return player
	 */
    """
    def getPlayer2(self):
        return self.player2


    """
    /**
	 * Method for making the players to complete their turn
	 * @return The player that needs to do the turn
	 */
    """
    def getDoTurn(self):
        return self.doTurn


    """
    /**
	 * Method to get the current state of the game. 
	 * @return GameEvent
	 */
  
    """
    def getEvent(self):
        return self.event


    """
    /**
	 * Method to print the board with all the pieces
	 * on the board.
	 */
    """
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



    """
    /**
	 * Method to play the game	 
	 */
    """
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
                
                
    """
    /**
	 * Method to check if the player is making a valid move 
	 * and not moving the enemy pieces
	 * @param move The move user tries to make
	 * @return The boolean value by checking the validity of the move.
	 */
  
    """

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
            print("The piece you selected is your opponent's. Please select a " +
                  player.getColor() + " piece.")
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
            print(
                "This move would leave your King in danger and thus cannot be performed")
            return False

        pieceMoved.move(move.getCurrentPos(), move.endPos)

        if endPiece != None:
            endPiece.pieceDied()

        move.getEndPos().setPiece(move.getPieceMoved())
        move.getCurrentPos().setPiece(None)

        print("Move successful")

        if isinstance(endPiece, King):
            self.event = GameEvent.WHITE_WIN

        else:
            self.event = GameEvent.BLACK_WIN

        # if game complete
        if self.getEvent() == GameEvent.BLACK_WIN or self.getEvent == GameEvent.WHITE_WIN:
            print("Game Complete")
            return True
        else:
            # otherwise swap players
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


    """
    /**
	  * Method to check if the destination is occupied by a friendly piece or not
	  * @param move The valid move of the player
	  * @param player The Player making the move
	  * @param pieceMoved The piece moved by the player
	  * @return false if there is not an ally (either empty or enemy)
	  */
   
    """
    def checkDestinationForAlly(move: Moves, player: Player, piecedMoved: Piece):
        if move.getEndPos().getOccupied() == False:
            return False

        if piecedMoved.getColorString() == move.getDestinationPiece().getColorString():
            return True

        return False

    # Checking collisions when moving pieces that can move multiple tiles

    """
    /**
	  * Method to check if any collisions happened or not.
	  * @param move The move player tries to make
	  * @param player The Player making the move
	  * @param pieceMoved The piece moved by the player
	  * @return  false if there are NOT any collisions
	  */
	 // returns false if there are NOT any collisions
    """
    def checkCollision(self, move: Moves, player: Player, pieceMoved: Piece):
        type = pieceMoved.getPieceType()
        destOcc = move.getEndPos().getOccupied()

        # Knight has no collision problem so quick check here
        if isinstance(type, PieceType.Knight) and destOcc == True:
            if pieceMoved.getPieceColor() == move.getDestinationPiece().getPieceColor():
                print("Spot is occupied by an ally. Cannot move.")
                return True
            return False

        # Get the range to move between col or rows
        changeRow = move.getEndPos().getRow() - move.getCurrentPos().getRow()
        changeCol = move.getEndPos().getCol() - move.getCurrentPos().getCol()

        # if piece moves vertical multiple tiles
        # (Pawn and King only move 1 so check is already done before, this applies
        # to Queen and Rook)

        if changeRow == 0:
            if changeCol > 0:
                for i in range(1, changeCol):
                    current_row = move.getCurrentPos().getRow()
                    current_col = move.getCurrentPos().getCol() + i
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])

                    if occupied:
                        print("Piece collided on the way to destination at: " + i)
                        return True
            else:
                for i in range(-1, changeCol, -1):
                    current_row = move.getCurrentPos().getRow()
                    current_col = move.getCurrentPos().getCol() + i
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)

        # Moving only in vertical direction
        elif changeCol == 0:
            if changeRow > 0:
                for i in range(1, changeRow):
                    current_row = move.getCurrentPos().getRow() + i
                    current_col = move.getCurrentPos().getCol()
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)

            else:
                for i in range(-1, changeRow, -1):
                    current_row = move.getCurrentPos().getRow() + i
                    current_col = move.getCurrentPos().getCol()
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)

        if abs(changeRow) == abs(changeCol):
            if changeRow > 0 and changeCol > 0:
                for i in range(1, changeRow):
                    current_row = move.getCurrentPos().getRow() + i
                    current_col = move.getCurrentPos().getCol() + i
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)
            elif changeRow < 0 and changeCol < 0:
                for i in range(-1, changeRow, -1):
                    current_row = move.getCurrentPos().getRow() + i
                    current_col = move.getCurrentPos().getCol() + i
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)
            elif changeRow < 0 and changeCol > 0:
                for i in range(1, changeCol):
                    current_row = move.getCurrentPos().getRow() - i
                    current_col = move.getCurrentPos().getCol() + i
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)
            elif changeRow > 0 and changeCol < 0:
                for i in range(1, changeRow):
                    current_row = move.getCurrentPos().getRow() + i
                    current_col = move.getCurrentPos().getCol() - i
                    occupied = self.isOccupied(
                        self.board[current_row][current_col])
                    self.ifOccupiedTrue(occupied)

        return False
    
    
    
    
    """
    /**
	  * Method to get whether king by checking all rows and columns that can reach king
	  * @param King piece that has location, tile, and color
	  * @return Whether king is in check
	  */
    
    """

    def kingInCheck(self, king: King):
        result = False
        kingTile = king.getCurrentTile()
        checkRow = kingTile.getRow()
        checkCol = kingTile.getCol()
        checkTile = kingTile
        checkForPiece = False
        checkPiece = None

        while checkRow > -1:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkRow = checkRow - 1

        checkRow = kingTile.getRow()
        
        while checkRow < 8:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkRow = checkRow + 1
            
            
        checkRow = kingTile.getRow()
        while checkCol > -1:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkCol = checkCol - 1
        
        checkCol = kingTile.getCol()
        while checkCol > -1:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkCol = checkCol + 1
            
            
        checkCol = kingTile.getCol()
        checkRow = kingTile.getRow()
        while checkCol < 8 and checkRow < 8:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkCol = checkCol + 1
            checkRow = checkRow + 1
            
            
        checkCol = kingTile.getCol()
        checkRow = kingTile.getRow()
        while checkCol > -1 and checkRow > -1:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkCol = checkCol - 1
            checkRow = checkRow - 1
            
            
        checkCol = kingTile.getCol()
        checkRow = kingTile.getRow()
        while checkCol > -1 and checkRow < 8:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkCol = checkCol - 1
            checkRow = checkRow + 1
            
            
        checkCol = kingTile.getCol()
        checkRow = kingTile.getRow()
        while checkCol < 8 and checkRow > -1:
            checkTile = self.board[checkRow][checkCol]
            checkForPiece = checkTile.getOccupied()

            if checkForPiece == True:
                checkPiece = checkTile.getPiece()
                if king.getColorString() == checkPiece.getColorString():
                    if checkPiece.isValidMove(checkTile, kingTile):
                        print(str(checkPiece))
                        king.setInCheck(True)
                        return True
                    else:
                        break
            else:
                break

            checkCol = checkCol - 1
            checkRow = checkRow + 1
            
        king.setInCheck(result)
        return result
            
            
        
            
            
            
        
            
    
    def ifOccupiedTrue(occupied):
        if occupied:
            print("Piece collided on the way to destination at: "+ i)
            return True
        
    
    def isOccupied(tile: Tile):
        if tile.getPiece() is not None:
            return True
        else: 
            return False
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                
