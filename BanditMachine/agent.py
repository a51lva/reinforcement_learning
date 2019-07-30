import numpy as np

class Agent:
    def __init__(self, bandit, epsilon):
        self.epsilon = epsilon
        self.k = np.zeros(bandit.total, dtype = np.int)
        self.q = np.zeros(bandit.total, dtype = np.float)
    
    def updateQ(self, action, reward):
        self.k[action] += 1
        self.q[action] += (1/self.k[action]) * (reward -self.q[action])
    
    def getAction(self, bandit, forceExplore = False):
        rand = np.random.random()
        if(rand < self.epsilon) or forceExplore:
            actionExplore = np.random.randint(bandit.total)
            return actionExplore
        else:
            actionGreedy = np.random.choice(np.flatnonzero(self.q == self.q.max()))
            return actionGreedy