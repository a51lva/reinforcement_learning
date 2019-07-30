import numpy as np

class Bandit:
    def __init__(self, success_probs):
        self.total = len(success_probs)
        self.probs = success_probs

    def getReward(self, action):
        rand = np.random.random()
        reward = 1 if (rand < self.probs[action]) else 0
        return reward
