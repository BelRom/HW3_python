import random
import time

def seed_time_random_agent(observation, configuration):
    random.seed(time.time())
    result = random.randrange(0, configuration.signs)    
    return result
