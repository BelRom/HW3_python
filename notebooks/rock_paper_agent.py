
def rock_paper_agent(observation, configuration):
    result = 0
    if observation.step % 2 == 0:
        result = 0
    else:
        result = 1
    return result
