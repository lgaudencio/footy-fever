import random

YES_OR_NO = ["YES", "NO"]

def in_game_scenario_one():
    response = ""
    chance = random.randint(0, 1)
    while response not in YES_OR_NO:
        response = input("You've been fouled inside the box do you chose to take the penatlty?... Please enter yes or no...")
        if response.upper() == "NO":
            print("You handed the responsiviluty to you teammate...")
            if chance == 0:
                print("You teammate missed the penalty!")
            elif chance == 1:
                print("You teammate scored! Your team is now 1-0 up!")
                break
        elif response.upper() == "YES":
            if chance == 0:
                print("You missed the penatly!")
                break
            elif chance == 1:
                print("You scored! Your team now leads 1-0")
                break
        else:
            print("Please type yes or no...")