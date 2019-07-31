import numpy as np

class Agent:
    def __init__(self, name, length, gama, epsilon):
        self.name = name
        self.q = np.zeros((3 , 3))
        self.length = length
        self.gama = gama 
        self.epsilon = epsilon
            
    def getAction(self, availableActions):
        return int(np.random.choice(availableActions, 1))
    
    def update(self, state, action):
        pass