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
    print(f"{suspicion} guard(s) were alerted of your position.")
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
        print("You enter the study. Working quickly and silently, you pull open a drawer labelled 'notes to self.'")
    else:
        print("You decided not to risk it.")
    return suspicion, clue

def crack_code(suspicion, code):
    newSuspicion = 0
    print(f"Hearing the guards, approach, you realize you only have time for {10-suspicion} guesses.")
    for i in range(10-suspicion):
        guess = input("You squint at the faded numbers on the panel and enter: ")
        if int(guess) == code:
            print(f"The screen reads: Attempt {i + 1}: Guess = {guess}... CORRECT")
            return newSuspicion, True
        else:
            print(f"The screen reads: Attempt {i + 1}: Guess = {guess}... INCORRECT")
            newSuspicion += 1
    newSuspicion += 3
    return newSuspicion, False

def escape(suspicion):
    danger = suspicion // 3
    progress = 0
    while progress < 10 and danger < 10:
        print(f"Danger: {danger}/10")
        print(f"Progress: {progress}/10")
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
                print("What you thought was a shortcut was a trap... many guards are chasing you!")
                danger += 3
    print(f"Danger: {danger}/10")
    print(f"Progress: {progress}/10")
    return progress

def heist(name):
    retry = True
    while retry:
        print(f"\nDr. Sinister has just finished building his doomsday device,\nand it's up to you, {name}, to steal the gemstone that powers it. \nYou've been able to locate his rather lavish secret lair, but without any eyes on the inside, it's going to be a tall order to break in.\n")
        print("======================================\n")
        code = random.randint(100,999)
        if DEBUG:
            print(f"Code: {code}")

        print("You see several ways in:")
        print("(1) A large, ornate front entrance sits slightly ajar. Seems too simple...")
        print("(2) A couple of shrubs, cut in the shape of Dr. Sinister's face, would make a great way to sneak in, but they wouldn't provide much cover.")
        print("(3) A window on the side of the building looks to be unlocked.")
        print("(4) The garden wall looks low enough to hop to get in the back.")
        print("(5) The drainpipe could be climbed, and you see a way in through the skylight.")
        print("(6) What seems to be an air vent unit outside could prove to be a good way in.")

        choice = int(input("Which way (1-6) will you try to enter?: "))
        print("")
        enterInfo = enter(choice, code)
        if enterInfo[1] == -2:
            print("You make your way in, and spot a small note with '>=500' scribbled on it")
        elif enterInfo[1] == -1:
            print("You make your way in, and spot a small note with '<500' scribbled on it")
        else:
            print(f"You make your way in, and overhear a conversation between guards: 'leftmost...digit...{enterInfo[1]}'")
        print(f"Current suspicion level: {enterInfo[0]}\n")
        print("======================================\n")

        investigate = False
        if input("You see a small room off to the side, which seems to be Dr. Sinister's study. It could have more info but seems risky... Do you investigate? Y/N: ") == "Y":
            investigate = True
        sideRoomInfo = side_room(investigate, code)
        if sideRoomInfo[1] >= 100:
            print(f"There is a note in the drawer: 'Remember code: {sideRoomInfo[1]}'")
        elif sideRoomInfo[1] >= 1:
            print(f"There is a note in the drawer: 'Remember code: XX{sideRoomInfo[1]}.' The first two digits are illegible")
        else:
            print("You found no new info.")
        print(f"Current suspicion level: {enterInfo[0] + sideRoomInfo[0]}\n")
        print("======================================\n")

        print("You turn a corner, climb a flight of stairs, and find the device.")
        print("It takes up much of the room, spanning the floor to the ceiling.")
        print("On its side is a small panel, which looks to accept a 3-digit code.")
        crackCodeInfo = crack_code(enterInfo[0] + sideRoomInfo[0], code)
        print(f"Current suspicion level: {crackCodeInfo[0]}\n")
        print("======================================\n")

        if crackCodeInfo[1] == True:
            print("The panel cracks open, revealing the bright red gemstone inside.")
        else:
            print("You rack your brain for anything you might have seen, but you come up short of the full code.")
        print("Suddenly, you hear a voice shout behind you. It's Dr. Sinister and his guards!")
        print("You're going to have to make a run for the exit. With all the twists and turns in Dr. Sinister's lair, you should be able to make it.")
        print("Making a straight run for it would be relatively safe, but you also see some spots you could hide to gether more info.")
        print("You also spotted some potential shortcuts on the way in, but who knows where they lead? Taking them would be risky.")
        if(escape(crackCodeInfo[0])) >= 10:
            print("You escaped!")
            retry = False
        else:
            print("You got caught...")
            if input("Do you want to retry? Y/N: ") == "Y":
                retry = True
            else:
                retry = False

print_signature("Nathaniel Willis", "400699857", "Engineering I", "Dr. Sam Scott", "Winter 2026 Term\n")
print("======================================\n")
user = input("Enter your name: ")
heist(user)