import numpy as np
import os
from game import Game as game
from agent import Agent as agent

if __name__ == "__main__":
    os.system('cls')
    print(' \n\t\t\tWelcome to the Tic Tac Toe Game.')
    
    board = np.zeros((3 , 3))
    agent = agent('Silva', 3, 0.8, 0.01)
    game = game(board, agent, 3)

    game.start()

    