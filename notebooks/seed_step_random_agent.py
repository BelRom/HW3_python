import random

def seed_step_random_agent(observation, configuration):
    random.seed(observation.step)
    return random.randrange(0, configuration.signs)
