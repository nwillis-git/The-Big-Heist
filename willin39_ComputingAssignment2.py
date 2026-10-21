import random

def enter(choice, code):
    clue = 0
    suspicion = 0
    for i in range(3):
        if random.randint(1,6) > choice:
            suspicion += 1
    if choice >= 4:
        if code >= 500:
            clue = -2
        else:
            clue = -1
    else:
        clue = code // 100
    print(f"{suspicion} guards were alerted of your position")
    return suspicion, clue