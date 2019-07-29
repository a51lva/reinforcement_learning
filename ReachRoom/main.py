import numpy as np
from rlModel import ReaforcementLearnModel as rlModel

if __name__ == "__main__":
    
    R = np.matrix([
        [-1, -1, -1, -1,  0, -1],
        [-1, -1, -1,  0, -1, 100],
        [-1, -1, -1,  0, -1, -1],
        [-1,  0,  0, -1,  0, -1],
        [ 0, -1, -1,  0, -1, 100],
        [-1,  0, -1, -1,  0, 100]
    ])

    Q = np.matrix(np.zeros([6,6]))

    rl = rlModel(R,Q,[0,1,2,3,4,5],[0,1,2,3,4,5], 0.8)

    print(R)
    
    #Training
    rl.training(10000)

    #print(rl.qMatrix / np.matrix(rl.qMatrix) * 100)

    #Testing
    currentState = rl.randomInitialState()
    print(rl.qMatrix / (np.max(rl.qMatrix) * 100))
    print('\nInitial State:' + str(currentState))
    steps = [currentState]

    while currentState != 5:
        next_step_index = rl.nextStepIndex(currentState)
        currentState = next_step_index
        steps.append(next_step_index)
        
    
    print('\nSelected path: ' + str(steps))