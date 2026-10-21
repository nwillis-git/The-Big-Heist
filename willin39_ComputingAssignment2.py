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

def crack_code(suspicion, code):
    newSuspicion = 0
    print(f"You have time for {10-suspicion} guesses")
    for i in range(10-suspicion):
        guess = input("Guess the code: ")
        if int(guess) == code:
            print(f"Attempt {i + 1}: Guess = {guess}, correct")
            return newSuspicion, True
        else:
            print(f"Attempt {i + 1}: Guess = {guess}, incorrect")
            newSuspicion += 1
    newSuspicion += 3
    return newSuspicion, False