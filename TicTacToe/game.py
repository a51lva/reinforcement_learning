class Game:
    def __init__(self, board, agent, length):
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
    
    def checkForWin(self):
        if self.winner != None:
            self.ended = True
            return True
        return False
    
    def checkForDraw(self):
        if self.winner != None and self.ended == True:
            return True
        return False
    
    def checkForEnd(self):
        return self.ended

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
        print(self.board)
    
    def playGame(self, agentStart = False):
        pass