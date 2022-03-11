
import sys 
from Model.Model import Model

if __name__ == '__main__':
    print("For this assignment we are simulating a chess game in console.")
    game = Model()
    game.printBoard()
    
    game.playGame()
    
