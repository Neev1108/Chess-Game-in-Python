from _typeshed import Self
from Model import Tile, King, Knight, Pawn, Queen, Bishop, Rook


class Board():
    whiteKing = ""
    blackKing = ""
    board = ""

    def __init__(self):
        self.board.createNewBoard()
        self.board.setPieces()

    def createNewBoard(self):
        r, c = 8, 8
        self.board = [[Tile(x, y, None) for x in range(r)] for y in range(c)]

    def setPieces(self):
        # set pawns
        for x in range(8):
            self.board[1][x] = Tile(1, x, Pawn(False))

        for x in range(8):
            self.board[6][x] = Tile(6, x, Pawn(True))

        # set black side
        self.board[0][4] = Tile(0, 4, King(False))
        self.board[0][3] = Tile(0, 3, Queen(False))
        self.board[0][0] = Tile(0, 0, Rook(False))
        self.board[0][7] = Tile(0, 7, Rook(False))
        self.board[0][1] = Tile(0, 1, Knight(False))
        self.board[0][6] = Tile(0, 6, Knight(False))
        self.board[0][2] = Tile(0, 2, Bishop(False))
        self.board[0][5] = Tile(0, 5, Bishop(False))

        # keep track of position of black King
        self.board[0][4].getPiece().setCurrentTile(self.board[0][4])
        self.blackKing = self.board[0][4].getPiece()

        # set white pieces
        self.board[7][4] = Tile(7, 4, King(True))
        self.board[7][3] = Tile(7, 3, Queen(True))
        self.board[7][0] = Tile(7, 0, Rook(True))
        self.board[7][7] = Tile(7, 7, Rook(True))
        self.board[7][1] = Tile(7, 1, Knight(True))
        self.board[7][6] = Tile(7, 6, Knight(True))
        self.board[7][2] = Tile(7, 2, Bishop(True))
        self.board[7][5] = Tile(7, 5, Bishop(True))

        # keep track of position of white King
        self.board[7][4].getPiece().setCurrentTile(self.board[7][4])
        self.whiteKing = self.board[7][4].getPiece()

    def getBoard(self):
        return self.board
    
    def getTile(self, x, y):
        return self.board[x][y]
    
    
    def getWhiteKing(self):
        return self.whiteKing
    
    def getBlackKing(self):
        return self.blackKing
    
    def setWhiteKing(self, k: King):
        self.whiteKing = k
        
    def setBlackKing(self, k: King):
        self.blackKing = k
        
