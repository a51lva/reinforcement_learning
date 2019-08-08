import numpy as np

class Game:
    def __init__(self, board, agent, length):
        self.length = length
        self.board = board
        self.agent = agent
        self.x = -1
        self.o = 1
        self.winner = None
        self.ended = False
        self.num_states = 3**(length * length)
    
    def start(self):
        print('\n\n\t\t\t*******Game started*******')
        print('\nAgent Name: '+str(self.agent.name))
        print('Board:')
        self.drawBoard()
    
    def checkForWin(self, length):
        if self.checkRows(length):
            return True
        elif self.checkColumns(length):
            return True
        elif self.checkDiagonals(length):
            return True
        elif self.checkForDraw:
            return True
        else:
            return False
    
    def checkForDraw(self):
        if np.all((self.board == 0) == False ):
            self.winner = None
            self.ended = True
            return True
        self.winner = None
        return False
    
    def checkForEnd(self):
        return self.ended

    def checkRows(self, length):
        for i in range(length):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*length:
                    self.winner = player
                    self.ended = True
                    return True
    
    def checkColumns(self, length):
        for i in range(length):
            for player in (self.x, self.o):
                if self.board[:,j].sum() == player*length:
                    self.winner = player
                    self.ended = True
                    return True
    
    def checkDiagonals(self, length):
        for player in (self.x, self.o):
            if self.board.trace() == player*length:
                self.winner = player
                self.ended = True
                return True
            
            if np.fliplr(self.board).trace() == player*length:
                self.winner = player
                self.ended = True
                return True

    def playerMove(self):
        pass
    
    def agentMove(self, action):
        pass
    
    def getReward(self, agent):
        if not self.checkForEnd():
            return 0
        return 1 if self.winner == agent else 0
    
    def isEmpty(self, i, j):
        return self.board[i,j] == 0
    
    def drawBoard(self):
        for i in range(self.length):
            print('-------------')
            for j in range(self.length):
                print(" ")
                if self.board[i, j] == self.x:
                    print("X"),
                elif self.board[i, j] == self.o:
                    print("O"),
                else:
                    print(" "),
            print("")
        print('-------------')
    
    def getState(self, length):
        k = 0
        h = 0

        for i in range(length):
            for j in range(length):
                if isEmpty(i, j):
                    v = 0
                elif self.board[i, j] == self.x:
                    v = 1
                elif self.board[i, j] == self.y:
                    v = 2
                h += (3**k) * v
                k += 1
        return h
    
    def playGame(self, agentStart = False):
        pass
    
    def gameOver(self):
        pass