
def shift_random_agent(observation, configuration):
    import random
    if observation.step == 0:
        return 0
    else:
        return (observation.lastOpponentAction + random.randrange(0, 100)) % 2
