import random
import math

DEBUG = False

def print_signature(name, studentNum, program, profName, currentTerm):
    print(f"Name: {name}")
    print(f"Student Number: {studentNum}")
    print(f"Program: {program}")
    print("ENG 1P13: Integrated Cornerstone Design Projects in Engineering")
    print(f"Professor: {profName}")
    print(f"Current Term: {currentTerm}")


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

def escape(suspicion):
    danger = suspicion // 3
    progress = 0
    while progress < 10 and danger < 10:
        action = input("Run, Hide, or Shortcut? ")
        if action == "Run" or action == "run":
            if random.randint(1,100) > 60:
                print("You covered some ground, but drew more attention to yourself.")
                danger += 1
            else:
                print("You covered some ground and weren't spotted.")
            progress += 1
        elif action == "Hide" or action == "hide":
            if random.randint(1,100) <= 80:
                print("You hid and gathered some more info")
                progress += 1
            else:
                print("You tried to hide, but you were spotted!")
                danger += 2
        elif action == "Shortcut" or action == "shortcut":
            if random.randint(1,100) <= 50:
                print("You took a hidden shortcut and bypassed many rooms.")
                progress += 3
            else:
                print("Not a smart shortcut... many guards are chasing you!")
                danger += 3
        if danger >= 10 or progress >= 10:
            return progress

def heist(name):
    retry = True
    while retry:
        print(f"Hello {name}, (this will be the greeting)")
        code = random.randint(100,999)
        if DEBUG:
            print(f"Code: {code}")

        choice = int(input("You see several ways in (inform the player of choices 1-6, and lower numbers are risky)"))
        enterInfo = enter(choice, code)
        if enterInfo[1] == -2:
            print("Clue: the code is 500 or greater")
        elif enterInfo[1] == -1:
            print("Clue: the code is less than 500")
        else:
            print(f"Clue: the leftmost digit of the code is {enterInfo[1]}")
        print(f"current suspicion level: {enterInfo[0]}")

        investigate = False
        if input("You see a room off to the side. You think it may have more info but seems risky... Do you investigate? Y/N: ") == "Y":
            investigate = True
        sideRoomInfo = side_room(investigate, code)
        if sideRoomInfo[1] >= 100:
            print(f"found whole code: {sideRoomInfo[1]}")
        elif sideRoomInfo[1] >= 1:
            print(f"found rightmost digit: {sideRoomInfo[1]}")
        else:
            print("You found nothing...")
        print(f"current suspicion level: {enterInfo[0] + sideRoomInfo[0]}")

        print("You're at the safe (code cracking)")
        crackCodeInfo = crack_code(enterInfo[0] + sideRoomInfo[0], code)
        print(f"current suspicion level: {crackCodeInfo[0]}")

        if crackCodeInfo[1] == True:
            print("Something about having broken in but having to escape")
        else:
            print("Something about having to escape despite not reaching your goal")
        if(escape(crackCodeInfo[0])) >= 10:
            print("You escaped!")
            retry = False
        else:
            print("You got caught...")
            retryPrompt = input("Do you want to retry? Y/N: ")
            if retryPrompt == "Y":
                retry = True
            else:
                retry = False

print_signature("Nathaniel Willis", "400699857", "Engineering 1", "Dr. Sam Scott", "Winter 2026 Term")
name = input("What's your name? ")
heist(name)