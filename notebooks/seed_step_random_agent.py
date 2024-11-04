
def seed_step_random_agent(observation, configuration):
    import random
    random.seed(observation.step)
    return random.randrange(0, 2)
