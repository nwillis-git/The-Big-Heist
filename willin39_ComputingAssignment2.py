import random
import math

def enter(choice, code):
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

def side_room(investigate, code):
    suspicion = 0
    clue = -1
    if investigate:
        investigateNum = random.randint(1,100)
        if investigateNum >= 81:
            clue = code
        elif investigateNum >= 31:
            clue = code % 10
        suspicion = math.ceil(investigateNum / 20)
        print("room description")
    else:
        print("skipped room")
    return suspicion, clue