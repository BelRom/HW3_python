
def seed_time_random_agent(observation, configuration):
    import random
    import time
    random.seed(time.time())
    result = random.randrange(0, 3)    
    print(f"seed_time_random_agent {result}")
    return result
