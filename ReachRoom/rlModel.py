import numpy as np
class ReaforcementLearnModel:
    def __init__(self, rMatrix, qMatrix, stateArray, actionArray, gamma):
        self.rMatrix = rMatrix
        self.qMatrix = qMatrix
        self.stateArray = stateArray
        self.actionArray = actionArray
        self.gamma = gamma

    def randomInitialState(self):
        return self.stateArray[np.random.randint(0, len(self.stateArray) - 1)]

    def calculateQ(self, state, action, max_value):
        self.qMatrix[state, action] = self.rMatrix[state, action] + self.gamma * max_value
    
    def availableActions(self, state):
        current_state_row = self.rMatrix[state]
        return np.where(current_state_row >= 0)[1]

    def sampleNextAction(self, availableActions):
        return int(np.random.choice(availableActions, 1))
    
    def nextStepIndex(self, state):
        max_index = np.where( self.qMatrix[state , ] == np.max(self.qMatrix[state, ]))[1]
        
        if max_index.shape[0] > 1:
            max_index = int( np.random.choice(max_index, size = 1))
        else:
            max_index = int(max_index)
        
        return max_index

    def update(self, state, action):
        max_index = self.nextStepIndex(action)        
        max_value = self.qMatrix[action, max_index]
        self.calculateQ(state, action, max_value)

    def training(self, _range):
        for i in range(_range):
            currentState = np.random.randint(0, int(self.qMatrix.shape[0]))
            available_act = self.availableActions(currentState)
            action = self.sampleNextAction(available_act)
            self.update(currentState, action)