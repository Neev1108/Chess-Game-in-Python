
from Model.Tile import Tile
from Model.Pieces import King, Queen, Rook, Knight, Bishop, Pawn


class Board():

    def __init__(self):
        self.createNewBoard()

    def createNewBoard(self):
        r, c = 8, 8
        self.board = [[Tile(x, y, None) for x in range(r)] for y in range(c)]
        self.setPieces()

    def setPieces(self):
        # set pawns
        for x in range(8):
            self.board[1][x] = Tile(1, x, Pawn.Pawn(False))

        for x in range(8):
            self.board[6][x] = Tile(6, x, Pawn.Pawn(True))

        # set black side
        self.board[0][4] = Tile(0, 4, King.King(False))
        self.board[0][3] = Tile(0, 3, Queen.Queen(False))
        self.board[0][0] = Tile(0, 0, Rook.Rook(False))
        self.board[0][7] = Tile(0, 7, Rook.Rook(False))
        self.board[0][1] = Tile(0, 1, Knight.Knight(False))
        self.board[0][6] = Tile(0, 6, Knight.Knight(False))
        self.board[0][2] = Tile(0, 2, Bishop.Bishop(False))
        self.board[0][5] = Tile(0, 5, Bishop.Bishop(False))

        # keep track of position of black King
        self.board[0][4].getPiece().setCurrentTile(self.board[0][4])
        self.blackKing = self.board[0][4].getPiece()

        # set white pieces
        self.board[7][4] = Tile(7, 4, King.King(True))
        self.board[7][3] = Tile(7, 3, Queen.Queen(True))
        self.board[7][0] = Tile(7, 0, Rook.Rook(True))
        self.board[7][7] = Tile(7, 7, Rook.Rook(True))
        self.board[7][1] = Tile(7, 1, Knight.Knight(True))
        self.board[7][6] = Tile(7, 6, Knight.Knight(True))
        self.board[7][2] = Tile(7, 2, Bishop.Bishop(True))
        self.board[7][5] = Tile(7, 5, Bishop.Bishop(True))

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
    
    def setWhiteKing(self, k: King.King):
        self.whiteKing = k
        
    def setBlackKing(self, k: King.King):
        self.blackKing = k
        
