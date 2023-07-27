import random

YES_OR_NO = ["YES", "NO"]
SHOOT_OR_PASS = ["SHOOT", "PASS"]

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


def in_game_scenario_two():
    response = ""
    chance = random.randint(0, 1)
    distance = str(random.randint(20, 45)) + " Yards"
    while response not in SHOOT_OR_PASS:
    response = input(f"Your team is battling it out to secure a Champions League spot for next season. A freekick has been awarded, it is {distance} out from goal. As the clubs freekick taker, you hover over the ball. Do you take a shot on goal or do you pass it?... Please enter shoot or pass...")
        if response.upper() == "SHOOT":
            print("You shoot...")
            if chance == 0:
                print("Goalkeeper saves it!")
            elif chance == 1:
                print("...You score! Your team is now 3-2 up!")
                break 
        elif response.upper() == "PASS":
            print("You pass to one of your teammates...")
            if chance == 0:
                print("An opposition player tackles your teammate, and gets the ball away!")
                 break
            elif chance == 1:
                print("Your teammate headers the ball and it goes in! Your team is now 3-2 up!")
                break
                
        else:
            print("Please type 'shoot' or 'pass'")