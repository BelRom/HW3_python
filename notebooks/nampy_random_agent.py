import numpy as np

def nampy_random_agent(observation, configuration):
    result = np.random.randint(0, configuration.signs)
    print(f"nampy_random_agent result {result}")
    return result
