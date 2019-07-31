class Game:
    def __init__(self, board, agent):
        self.board = board
        self.agent = agent
    
    def start(self):
        print('\n\n\t\t\t*******Game started*******')
        print('\nAgent Name: '+str(self.agent.name))
        print('Board:')
        self.drawBoard()
    
    def checkForWin(self, parameter_list):
        pass
    
    def checkForDraw(self, parameter_list):
        pass
    
    def checkForEnd(self, parameter_list):
        pass

    def playerMove(self):
        pass
    
    def agentMove(self, action):
        pass
    
    def drawBoard(self):
        print(self.board)