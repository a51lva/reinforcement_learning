import numpy as np
import os
from game import Game as game
from agent import Agent as agent

if __name__ == "__main__":
    os.system('cls')
    print(' \n\t\t\tWelcome to the Tic Tac Toe Game.')
    
    board = np.matrix([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
    agent = agent('Silva')
    game = game(board, agent)

    game.start()

    