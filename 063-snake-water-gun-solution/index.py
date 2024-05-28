import random

computer_choice = random.randint(0, 2)
user_choice = int(input("0 for Snake, 1 for Water and 2 for Gun: "))


def check(computer, user):
    if computer == user:
        return 0

    if computer == 0 and user == 1:
        return -1

    if computer == 1 and user == 2:
        return -1

    if computer == 2 and user == 0:
        return -1

    return 1


score = check(computer_choice, user_choice)
if score == 0:
    print("DRAW!")
elif score == -1:
    print("LOOSE!")
else:
    print("WIN!")
