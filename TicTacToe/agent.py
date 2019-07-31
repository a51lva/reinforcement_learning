import numpy as np

class Agent:
    def __init__(self, name):
        self.name = name
            
    def getAction(self, availableActions):
        return int(np.random.choice(availableActions, 1))
    
    def update(self, state, action):
        pass