
def oposite_agent(observation, configuration):
    if observation.step == 0:
        return 2
    if observation.lastOpponentAction == 0:
        return 1
    elif observation.lastOpponentAction == 1:
        return 2
    else:
        return 0
