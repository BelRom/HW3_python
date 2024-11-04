
def order_rock_scissors_paper_agent(observation, configuration):
    result = 0
    if observation.step % 3 == 0:
        result = 0
    if observation.step % 2 == 0:
        result = 1
    else:
        result = 2
    return result
