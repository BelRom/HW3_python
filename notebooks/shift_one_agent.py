
def shift_one_agent(observation, configuration):
    if observation.step == 0:
        return 1
    else:
        return observation.lastOpponentAction + 1 % 3
