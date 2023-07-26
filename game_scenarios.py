import random

YES_OR_NO = ["YES", "NO"]

def in_game_scenario_one():
    response = ""
    chance = random.randint(0, 1)
    while response not in YES_OR_NO:
        response = input("You've been fouled inside the box do you chose to take the penatlty?... Please enter yes or no...")
        if response.upper() == "NO":
        
        elif response.upper() == "YES":

        else:
            print("Please type yes or no...")