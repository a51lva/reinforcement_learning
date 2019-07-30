import numpy as np
from bandit import Bandit as Bandit
from agent import Agent as Agent

def experiment(bandit, agent, n_episodes):
    action_history = []
    reward_history = []

    for episode in range(n_episodes):
        action = agent.getAction(bandit)
        reward = bandit.getReward(action)
        agent.updateQ(action, reward)

        action_history.append(action)
        reward_history.append(reward)
    return (np.array(action_history), np.array(reward_history))


if __name__ == "__main__":
    print('Hello My Awesome Casino Machine')

    bandit_probs = [0.10, 0.50, 0.60, 0.80, 0.10, 0.25, 0.60, 0.45, 0.75, 0.65]
    experiments = 100
    episodes = 10000
    epsilon = 0.1

    n_bandits = len(bandit_probs)
    print("Running multi-armed bandits with N_bandits = {} and agent epsilon = {}".format(n_bandits, epsilon))
    
    reward_history_avg = np.zeros(episodes)
    action_history_sum = np.zeros((episodes, n_bandits))

    for i in range(experiments):
        bandit = Bandit( bandit_probs )
        agent = Agent(bandit, epsilon)
        (action_history, reward_history) = experiment(bandit, agent, episodes)

        if ( i + 1) % (experiments / 100) == 0:
           print("[Experiment {}/{}]".format(i + 1, experiments))
           print("  N_episodes = {}".format(episodes))
           print("  bandit choice history = {}".format(action_history + 1))
           print("  reward history = {}".format(reward_history))
           print("  average reward = {}".format(np.sum(reward_history) / len(reward_history)))
           print("") 
        
        reward_history_avg += reward_history
        
        for j, (a) in enumerate(action_history):
            action_history_sum[j][a] += 1
    
    reward_history_avg /= np.float(experiments)
    print("reward history avg = {}".format(reward_history_avg))        
        
