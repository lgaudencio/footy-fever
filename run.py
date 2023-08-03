import random
import os
import time
import stats as stat
import game_scenarios as scenario
from colorama import Fore, Back, Style, init
import pyfiglet

init(autoreset=True)

MAIN_MENU_OPTIONS = ["1", "2", "3"]
CLUB_OPTIONS = ["1", "2"]
YES_OR_NO = ["YES", "NO"]
CLUB_ONE = ["BENFICA", "AJAX", "RB SALZBURG"]
CLUB_TWO = ["CHELSEA", "LIVERPOOL", "ARSENAL"]
CLUB_THREE = ["REAL MADRID", "BARCELONA", "BAYERN MUNCHEN"]
RANDOM_OPPONENT = ["AC MILAN", "JUVENTUS", "BORUSSIA DORTMUND", "FC PORTO"]

SPONSORSHIP_DEAL = ["NIKE", "ADIDAS", "PUMA"]

class End_Club:
    def __init__(self, club, city, country):
        self.club = club
        self.city = city
        self.country = country

saudi_club = End_Club("AL-NASSR", "RIYADH", "SAUDI ARABIA")
usa_club = End_Club("INTER MIAMI", "MIAMI", "USA")

name = ""
age = 17

weekly_wage_one = ""
weekly_wage_two = ""
weekly_wage_three = ""

award = ""

def introduction():
    # print("Footy Fever")
    game_title = pyfiglet.figlet_format("Footy Fever", font="standard", justify="center")
    print(Fore.GREEN + Style.BRIGHT + game_title)
    
    main_menu()
    input_name()

    input("Press Enter to continue...\n")
    time.sleep(1)
    print("Loading Chapter 1...\n")
    time.sleep(3)

    start_pro_career()


def main_menu():
    response = ""
    while response not in MAIN_MENU_OPTIONS:
        print("\nMAIN MENU\n")
        response = input("""Please select an option below:
    
Enter 1 - About This Game
Enter 2 - Game Instructions
Enter 3 - Play Game
""")
        if response == "1":
            print("About This Game:")
            print("""Welcome to Football Glory, a text-based game that will take 
you to the heights of European Football. 

Will you reach lengednary status and have your name 
cemented alongside the European Elite?

There's only one way to find out!\n""")
            invalid_main_menu_input()
            main_menu()
        elif response == "2":
            print("Game instructions")
            invalid_main_menu_input()
            main_menu()
        elif response == "3":
            print("\nStarting Game...\n")
            time.sleep(3)
            break
        else:
            print(Fore.RED + "\nError: Please enter a either 1, 2 or 3")


def invalid_main_menu_input():
    while True:
        try:
            response = input("Please enter 0 to go back to the Main Menu... ")
            if response == "0":
                break
            else:
                None
        except Exception:
            print(Fore.RED + "Error: Please enter a valid input...")
            main_menu()


def input_name():
    global name
    while True:
        name = input("Please enter your name?: ")
        if len(name) > 0:
            print(f"""\nWelcome {name}!
        
You will now begin your path to stardom, good luck in your journey!\n""")
            break
        else:
            print(Fore.RED + "\nError: Name must be longer than 0 characters!\n")


def weekly_wage_club_one():
    global weekly_wage_one
    global weekly_wage_two
    global weekly_wage_three

    weekly_wage_one = (random.randint(5, 11)) * 1000
    weekly_wage_two = (random.randint(5, 11)) * 1000
    weekly_wage_three = (random.randint(5, 11)) * 1000


def start_pro_career():
    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 1: The Choice ")

    time.sleep(2)

    # print(f"{name}, you have just finished a successful youth career at your\nlocal football club.")

    print(f"""\n{name}, you have just finished a successful youth career
at your local football club.\n""")

    time.sleep(4)

    # print("Alongside your talent, your agent has been very proactive\nand there are a number of clubs around Europe that would\nlike to sign you.")

    print("""Alongside your talent, your agent has been very proactive and
there are a number of clubs around Europe that would like to sign you.\n""")

    time.sleep(4)

    weekly_wage_club_one()

    print(f"""Three clubs have expressed their interest and they have 
guaranteed that you'll play at least 50% of the games in your first season. 

Please see your options below:
\nOption 1: {CLUB_ONE[0]} for £{weekly_wage_one} per week
\nOption 2: {CLUB_ONE[1]} for £{weekly_wage_two} per week  
\nOption 3: {CLUB_ONE[2]} for £{weekly_wage_three} per week""")

    time.sleep(2)

    club_picked = ""
    while club_picked not in CLUB_ONE:
        club_picked = input("\nTo pick a team, please type one of the following: Benfica, Ajax or RB Salzburg\n")
        if club_picked.upper() == "BENFICA":
            print("\nYou are heading to Lisbon, Portugal. Good luck in the upcoming season!\n")
            scenario.in_game_scenario_one()
            break
        elif club_picked.upper() == "AJAX":
            print("\nYou are heading to Amsterdam, Netherlands. Good luck in the upcoming season!\n")
            scenario.in_game_scenario_one()
            break
        elif club_picked.upper() == "RB SALZBURG":
            print("\nYou are heading to Salzburg, Austria. Good luck in the upcoming season!\n")
            scenario.in_game_scenario_one()
            break
        else:
            print(Fore.RED + "\nError: Please select a club option from above!\n")

    input("\nPress Enter to continue...\n")
    time.sleep(1)

def club_one_end():
    global age
    age += 5

    print("Loading Chapter 2...\n")

    time.sleep(3)

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 2: A STAR IN THE MAKING ")

    time.sleep(2)

    print("\nFive years later...\n")

    time.sleep(2)

    stat.club_one_stats()

    input("\nPress Enter to continue...\n")


def start_club_two():
    print("Loading Chapter 3...\n")

    time.sleep(3)

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 3: BIG MONEY MOVE ")

    transfer_fee = "£" + str(random.randint(55, 80)) + " Million"
    second_club = random.choice(CLUB_TWO)

    print("""\nYou are currently preparing for a pre-season tour 
when you get a call from your agent.\n""")

    time.sleep(2)

    print("""Your agent tells you that some big Premier League clubs 
are battling it out for your signature!\n""")

    time.sleep(2)

    print(f"""You've been told that your current club has accepted a 
fee of {transfer_fee} from {second_club}.\n""")

    time.sleep(3)

    global weekly_wage_one
    weekly_wage_one = "£" + str(random.randint(150, 200)) + "k"

    negotiated_salary = "£" + str(random.randint(150, 200)) + "k"

    response = ""
    while response not in YES_OR_NO:
        response = input(f"""{second_club} are offering you a weekly salary of {weekly_wage_one}.

Do you accept this offer or do you risk negotiating?
      
If you accept the offer type 'YES' if you want to negotiate type 'NO'\n""")

        if response.upper() == "NO":
            if negotiated_salary < weekly_wage_one:
                print(f"""\n{second_club} are not impressed with the negotiations, 
so they have now offered you {negotiated_salary}\n""")
                print(f"""Congratulations {name}, you will now meeting up with your 
new teammates at {second_club}!\n""")
                break
            elif negotiated_salary > weekly_wage_one:
                print(f"""\n{second_club} are impressed by your negotiating skills, 
they have now offered {negotiated_salary}\n""")
                print(f"""Congratulations {name}, you will now meeting up with your 
new teammates at {second_club}!\n""")
                break
            else:
                print(f"The offer stands at {weekly_wage_one}, {second_club} will not negotiate!")
                print(f"""Congratulations {name}, you will now meeting up with your 
new teammates at {second_club}!""")
        elif response.upper() == "YES":
            print(f"""\nCongratulations {name}, you will now meeting up with your 
new teammates at {second_club}!\n""")
            break
        else:
            print(Fore.RED + "\nError: Please enter either YES or NO\n")
    
    input("Press Enter to continue...")


def at_club_two():
    print("\nLoading Chapter 4...\n")

    time.sleep(3)

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 4: HIGH FLYER ")

    sponsor = random.choice(SPONSORSHIP_DEAL)
    sponsor_salary = "£" + str(random.randint(1, 5)) + " Million"

    print(f"""\nYour big money move to has made headlines.
  
{sponsor} has contacted you and would like to offer you a sponsorship
deal worth {sponsor_salary} per year.\n""")

    response = ""
    while response not in YES_OR_NO:
        response = input(f"""{name}, would you like to sign on with {sponsor}? 
Please type 'YES' or "NO'\n""")
        if response.upper() == "YES":
            print(f"\nCongratulation {name}, you've signed a lucrative deal with {sponsor}!\n")
            break
        elif response.upper() == "NO":
            print(f"\nYou've decided to turn down a lucrative sponsor from {sponsor}.\n")
            break
        else:
            print("Error: Please enter either YES or NO\n")

    # time.sleep(2)

    # print("Loading in-game scenario...")

    # time.sleep(3)

    scenario.in_game_scenario_two()

    time.sleep(2)

    input("Press Enter to continue...\n")

    time.sleep(2)

    print("Loading award ceremony...\n")

    time.sleep(3)

    print(f"{name}, you have been nominated for UEFA Player of the Year Award.\n")

    global award
    award = "UEFA Player of the Year"
    award_time()


def award_time():
    # global award
    # award = "UEFA Player of the Year"
    award_placement = random.randint(1, 3)

    print(f"""{name}, you have arrived in France for the {award} ceremony. 
Tonight, you are among teammates and rivals to see who will take home the 
{award} award.\n""")

    time.sleep(2)

    print("Top 3 is about to be announced...\n")

    time.sleep(3)

    if award_placement == 1:
        print(f"""Congratulations {name}! You've won the {award}. 
You've cemented your name amongst the great that have won this award!\n""")
    elif award_placement == 2:
        print(f"{name}, you've finished in 2nd place\n")
    else:
        print(f"{name}, you've finished in 3rd place\n")

    time.sleep(2)

    input("Press Enter to continue...")


def end_second_club(): 
    global age
    age += 5
    third_club = random.choice(CLUB_THREE)
    release_clause = "£" + str(random.randint(100, 150)) + " Million"
    random_opponent = random.choice(RANDOM_OPPONENT)
    negotiated_salary = "£" + str(random.randint(400, 500)) + "k"

    global weekly_wage_one
    weekly_wage_one = "£" + str(random.randint(400, 500)) + "k"

    print(f"""\n{name}, you are on your back from playing a first leg away game against 
{random_opponent} in the UEFA Champions League Quarter Finals.\n""") 

    time.sleep(2)

    print(f"""Your agent informs you that {third_club} has approched your current club 
and will pay your release clause of {release_clause}.\n""")

    time.sleep(2)

    print(f"""A few days later, the Sporting Director of your current club pulls you aside 
for a meeting. He informs you that as {third_club} paid your release clause and 
you are free to join them.\n""")

    time.sleep(2)

    response = ""
    while response not in YES_OR_NO:
        response = input(f"""{third_club} are offering you a weekly salary of {weekly_wage_one}.

Do you accept this offer or do you risk negotiating?
      
If you accept the offer type 'YES' if you want to negotiate type 'NO'\n""")
        if response.upper() == "NO":
            if negotiated_salary < weekly_wage_one:
                print(f"""\n{third_club} are not impressed with the negotiations, 
so they have now offered you {negotiated_salary}\n""")
                print(f"Congratulations {name}, you are now heading to your new club!\n")
                break
            elif negotiated_salary > weekly_wage_one:
                print(f"""\n{third_club} are impressed by your negotiating skills, 
they have now offered {negotiated_salary}\n""")
                print(f"Congratulations {name}, you are now heading to your new club!\n")
                break
            else:
                print(f"\nThe offer stands at {weekly_wage_one}, {third_club} will not negotiate!\n")
                print(f"Congratulations {name}, you are now heading to your new club!\n")
        elif response.upper() == "YES":
            print(f"Congratulations {name}, you are now heading to your new club!")
            break
        else:
            print(Fore.RED + "\nError: Please enter either YES or NO")

    print(f"""\n{name}, as you move to {third_club}, you are reminded with what you have 
achieved in the last five season with your previous club...\n""")

    stat.club_two_stats()

    input("\nPress Enter to continue...\n")


def at_third_club():
    print("Loading Chapter 5...\n")

    time.sleep(3)

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 5: SO THIS IS PEAKING? ")

    scenario.in_game_scenario_three()

    time.sleep(2)

    input("\nPress Enter to continue...\n")

    print(f"""{name}, you had a phenominal season and you've been nominated for the 
Balon d'Or, the most presigious prize in world football!

While at the ceremony you meet with great stars of the beautiful game, but, 
on this night they are also your rivals. Let's see who comes out on top!""")

    time.sleep(3)

    global award
    award = "Balon d'Or"

    award_time()


def end_third_club():
    global age
    age += 5

    print("Loading Chapter 6...\n")

    time.sleep(3)

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 6: A NEW ADVENTURE AWAITS ")

    print(f"""\nAs you are now {age} years old, your club is reluctant to give you the 
contract extention you wanted, and clubs around the world have got wind of 
this information...\n""")

    time.sleep(2)

    print(f"""{name}, you have two lucrative deals on the table 
and you need to select one of them...\n""")

    time.sleep(2)

    input("Press Enter to view the first option...\n")

    print("FIRST OPTION:\n")

    print(f"""{saudi_club.club}, who are based in {saudi_club.city}, {saudi_club.country} 
are willing to give you a yearly salary of £100 Million and give you a role 
as a football ambassador for the region.\n""")

    time.sleep(2)

    input("Press Enter to view the second option...\n")

    print("SECOND OPTION:\n")

    print(f"""{usa_club.club}, who are used in {usa_club.city}, {usa_club.country} 
are wiling to give you a yearly salary of £50 Million, 
but you will also have the following: stock shares of the club, 
a sponsorship deal with Apple and you get to keep your image rights.\n""")

    response = ""
    while response not in CLUB_OPTIONS:
        response = input(f"{name}, which option would you like to pick? Please type 1 or 2\n")
        if response == "1":
            print(f"""\n{name}, you have decided to joing {saudi_club.club}. 
You will now be meeting up with your new colleagues in 
{saudi_club.city}, {saudi_club.country}. 
We wish you the best of luck!\n""")
        elif response == "2":
            print(f"""\n{name}, you have decided to joing {usa_club.club}. 
You will now be meeting up with your new colleagues in 
{usa_club.city}, {usa_club.country}. 
We wish you the best of luck!\n""")
        else:
            print(Fore.RED + "Error: Please enter either 1 or 2\n")

    print(f"""{name}, on the last day at your current club, teammates and fans gather, 
your accolades are read out by the clubs president...\n""")

    time.sleep(2)

    stat.club_three_stats()


def career_end():
    global age
    age += 5

    print("Loading Chapter 7...")

    time.sleep(3)

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + " CHAPTER 7: THE LEGACY ")

    scenario.in_game_scenario_four()

    print("A few years later...\n")

    print(f""" ***BREAKING NEWS***

{name} has just announced their retirement at the age of {age}. 

Over the past five years playing in a different continent, 
{name} has achieved the following titles...\n""")

    stat.club_four_stats()

    print("""\nThroughout their career, the amount of titles won have been the following...\n""")

    stat.total_career_titles()


def play_again():
    print("\nYou have now completed the game!\n")
    response = ""
    while response not in YES_OR_NO:
        response = input("Would you like to play again?\n")
        if response.upper() == "YES":
            print("Loading new game...")
            os.system('clear')
            introduction()
        elif response.upper() == 'NO':
            print("\nThank you for playing!")
            exit()
        else:
            print(Fore.RED + "\nError: Please enter YES or NO")

def main():
    introduction()

    club_one_end()

    start_club_two()

    at_club_two()

    end_second_club()

    at_third_club()

    end_third_club()

    career_end()

    play_again()

if __name__ == "__main__":
    main()

    