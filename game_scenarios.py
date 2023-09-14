import random
import time
from colorama import Fore, Back, Style, init

YES_OR_NO = ["YES", "NO"]
SHOOT_OR_PASS = ["SHOOT", "PASS"]


def in_game_scenario_one():
    """
    This function is used for the first in-game scenario, where
    the user will have two options to chose from and output
    generated at random
    """
    time.sleep(2)
    print(Fore.CYAN + Style.BRIGHT + "Loading in-game scenario...\n")
    time.sleep(2)
    response = ""
    chance = random.randint(0, 1)
    while response not in YES_OR_NO:
        response = input(
            "You've been fouled inside the box do you chose to "
            "take the penalty or hand it to a teammate?...\n"
            "\nPlease enter YES to take the penalty or NO to hand it over to "
            "your teammate...\n")
        if response.upper() == "NO":
            print("\nYou handed the responsibility to your teammate...\n")
            time.sleep(1)
            if chance == 0:
                print("Your teammate missed the penalty! Score stays at 0-0")
                break
            elif chance == 1:
                print("You teammate scored! Your team is now 1-0 up!")
                break
        elif response.upper() == "YES":
            print("\nYou place the ball on the spot...\n")
            time.sleep(1)
            if chance == 0:
                print("You missed the penalty!")
                break
            elif chance == 1:
                print("You scored! Your team now leads 1-0")
                break
        else:
            print(Fore.RED + "Error: Please enter either YES or NO...")

    time.sleep(2)


def in_game_scenario_two():
    """
    This function is used for the second in-game scenario, where
    the user will have two options to chose from and output
    generated at random
    """
    time.sleep(2)
    print(Fore.CYAN + Style.BRIGHT + "Loading in-game scenario...\n")
    time.sleep(2)
    response = ""
    chance = random.randint(0, 1)
    distance = str(random.randint(20, 45)) + " Yards"
    while response not in SHOOT_OR_PASS:
        response = input(
            "Your team is battling to secure a Champions League spot for "
            "next season.\n"
            f"\nA freekick has been awarded, it is {distance} out from goal.\n"
            "\nAs the clubs freekick taker, you hover over the ball. "
            "Do you take a shot on goal or do you pass it?...\n"
            "\nPlease enter SHOOT or PASS...\n")
        if response.upper() == "SHOOT":
            print("\nYou shoot...\n")
            time.sleep(1)
            if chance == 0:
                print("Goalkeeper saves it!\n")
                break
            elif chance == 1:
                print("...You score! Your team is now 3-2 up!\n")
                break
        elif response.upper() == "PASS":
            print("\nYou pass to one of your teammates...\n")
            time.sleep(1)
            if chance == 0:
                print(
                    "An opposition player tackles your teammate, and gets "
                    "the ball away!\n")
                break
            elif chance == 1:
                print(
                    "Your teammate headers the ball and it goes in! Your "
                    "team is now 3-2 up!\n")
                break
        else:
            print(Fore.RED + "\nPlease enter either SHOOT or PASS...\n")

    time.sleep(2)


def in_game_scenario_three():
    """
    This function is used for the third in-game scenario, where
    the user will have two options to chose from and output
    generated at random
    """
    time.sleep(2)
    print(Fore.CYAN + Style.BRIGHT + "\nLoading in-game scenario...\n")
    time.sleep(2)
    response = ""
    chance = random.randint(0, 1)
    while response not in YES_OR_NO:
        response = input(
            "An opposition player is in on goal, do you tackle him?...\n"
            "\nPlease enter YES to tackle or NO to take no action...\n")
        if response.upper() == "YES":
            print("\nYou decided to make the tackle...\n")
            time.sleep(1)
            if chance == 0:
                print(
                    "Bad tackle! You got none of the ball so the ref gave "
                    "you a red card!\n")
                break
            elif chance == 1:
                print("\nYou got the ball! Excellent tackle!\n")
                break
        elif response.upper() == "NO":
            print(
                "\nThe opposition player has a great chance to score "
                "here...\n")
            time.sleep(1)
            if chance == 0:
                print(
                    "The opposition player scored, your team is now 2-1 "
                    "down!\n")
                break
            elif chance == 1:
                print(
                    "You goalkeeper made an incredible save, the score "
                    "stays level at 1-1!\n")
                break
        else:
            print(Fore.RED + "\nPlease enter either YES or NO...")

    time.sleep(2)


def in_game_scenario_four():
    """
    This function is used for the fourth in-game scenario, where
    the user will have two options to chose from and output
    generated at random
    """
    time.sleep(2)
    print(Fore.CYAN + Style.BRIGHT + "\nLoading in-game scenario...\n")
    time.sleep(2)
    response = ""
    chance = random.randint(0, 1)
    while response not in SHOOT_OR_PASS:
        response = input(
            "You are one-on-one with the goalkeeper, but the angle is "
            "getting tighter.\n"
            "\nYou see that if you pass to your teammate, they'll have an a "
            "clear cut\n"
            "opportunity to score. Do you take the shot or do you pass to "
            "teammate?...\n"
            "\nPlease enter SHOOT or PASS...\n")
        if response.upper() == "SHOOT":
            print("\nYou shoot...\n")
            time.sleep(1)
            if chance == 0:
                print("The shot goes wide!\n")
                break
            elif chance == 1:
                print("...You score! Your team is now 4-3 up!\n")
                break
        elif response.upper() == "PASS":
            print("\nYou pass to your teammate...\n")
            time.sleep(1)
            if chance == 0:
                print("You teammate shoots the ball over the bar!\n")
                break
            elif chance == 1:
                print(
                    "Your teammate gets an easy tap in and your team now "
                    "leads by 4-3!\n")
                break
        else:
            print(Fore.RED + "\nError: Please type SHOOT or PASS...")

    time.sleep(2)
