import random

YES_OR_NO = ["YES", "NO"]
SHOOT_OR_PASS = ["SHOOT", "PASS"]

def in_game_scenario_one():
    time.sleep(3)
    print("Loading in-game scenario...")
    time.sleep(3)
    response = ""
    chance = random.randint(0, 1)
    while response not in YES_OR_NO:
        response = input("You've been fouled inside the box do you chose to take the penatlty?... Please enter yes or no...")
        if response.upper() == "NO":
            print("You handed the responsiviluty to you teammate...")
            time.sleep(2)
            if chance == 0:
                print("You teammate missed the penalty!")
                break
            elif chance == 1:
                print("You teammate scored! Your team is now 1-0 up!")
                break
        elif response.upper() == "YES":
            print("You place the ball on the spot...\n")
            time.sleep(2)
            if chance == 0:
                print("You missed the penatly!")
                break
            elif chance == 1:
                print("You scored! Your team now leads 1-0")
                break
        else:
            print("Please type yes or no...")


def in_game_scenario_two():
    time.sleep(3)
    print("Loading in-game scenario...")
    time.sleep(3)
    response = ""
    chance = random.randint(0, 1)
    distance = str(random.randint(20, 45)) + " Yards"
    while response not in SHOOT_OR_PASS:
    response = input(f"Your team is battling it out to secure a Champions League spot for next season. A freekick has been awarded, it is {distance} out from goal. As the clubs freekick taker, you hover over the ball. Do you take a shot on goal or do you pass it?... Please enter shoot or pass...")
        if response.upper() == "SHOOT":
            print("You shoot...")
            time.sleep(2)
            if chance == 0:
                print("Goalkeeper saves it!")
                break
            elif chance == 1:
                print("...You score! Your team is now 3-2 up!")
                break 
        elif response.upper() == "PASS":
            print("You pass to one of your teammates...")
            time.sleep(2)
            if chance == 0:
                print("An opposition player tackles your teammate, and gets the ball away!")
                break
            elif chance == 1:
                print("Your teammate headers the ball and it goes in! Your team is now 3-2 up!")
                break        
        else:
            print("Please type 'shoot' or 'pass'")


def in_game_scenario_three():
    time.sleep(3)
    print("Loading in-game scenario...")
    time.sleep(3)
    response = ""
    chance = random.randint(0, 1)
    while response not in YES_OR_NO:
        response = input("An opposition player is in on goal, do you takle him?... Please enter yes or no...")
        if response.upper() == "YES":
            print("You decided to make the tackle...")
            time.sleep(2)
            if chance == 0:
                print("Bad tackle! You got none of the ball so the ref gave you a red card!")
                break
            elif chance == 1:
                print("You got the ball! Excellent tackle!")
                break
        elif response.upper() == "NO":
            print("The opposition player has a great chance to score here...")
            time.sleep(2)
            if chance == 0:
                print("The opposition player scored, your team is now 2-1 down!")
                break
            elif chance == 1:
                print("You goalkeeper made an incredible save, the score stays level at 1-1!")
                break
        else:
            print("Please type YES or NO...")


def in_game_scenario_four():
    response = ""
    chance = random.randint(0, 1)
    while response not in SHOOT_OR_PASS:
        response = input("You find yourself one-on-one with the goalkeeper, but the angle is getting tighter. You see that if you pass to your teammate, they'll have an a clear cut opportunity to score. Do you take the shot or do you pass?... Please enter shoot or pass...")
        if response.upper() == "SHOOT":
            print("You shoot...")
            if chance == 0:
                print("The shot goes wide!")
                break
            elif chance == 1:
                print("...You score! Your team is now 4-3 up!")
                break
        elif response.upper() == "PASS":
            print("You pass to your teammate...")
            if chance == 0:
                print("You teammate shoots the ball over the bar!")
                break
            elif chance == 1:
                print("Your teammate gets an easy tap in and your team now leads by 4-3!")
                break          
        else:
            print("Please type SHOOT or PASS")