import random
import stats as stat

MAIN_MENU_OPTIONS = ["1", "2", "3"]
YES_OR_NO = ["YES", "NO"]
CLUB_ONE = ["BENFICA", "AJAX", "RB SALZBURG"]
CLUB_TWO = ["CHELSEA", "LIVERPOOL", "ARSENAL"]

SPONSORSHIP_DEAL = ["NIKE", "ADIDAS", "PUMA"]

name = ""
age = 17

weekly_wage_one = ""
weekly_wage_two = ""
weekly_wage_three = ""

def introduction():
    print("Footy Fever")
    main_menu()
    input_name()
    start_pro_career()


def main_menu():
    response = ""
    while response not in MAIN_MENU_OPTIONS:
        print("MAIN MENU")
        response = input("""Please select an option below:
    
Enter 1 - About This Game
Enter 2 - Game Instructions
Enter 3 - Play Game
""")
        if response == "1":
            print("About This Game:")
            invalid_main_menu_input()
        elif response == "2":
            print("Game instructions")
            invalid_main_menu_input()
        elif response == "3":
            print("Starting Game...")
        else:
            print("Please enter a number between 1 and 3")


def invalid_main_menu_input():
    while True:
        try:
            response = input("Please enter 0 to go back to the Main Menu... ")
            if response == "0":
                break
            else:
                None
        except Exception:
            print("Please enter valud input...")


def input_name():
    global name
    while True:
        name = input("Please enter your name?: ")
        if len(name) > 0:
            print(f"""Welcome {name}!
        
You will now begin your path to stardom, good luck in your journey!""")
            break
        else:
            print("Name must be longer than 0 characters!")


def weekly_wage_club_one():
    global weekly_wage_one
    global weekly_wage_two
    global weekly_wage_three

    weekly_wage_one = (random.randint(5, 11)) * 1000
    weekly_wage_two = (random.randint(5, 11)) * 1000
    weekly_wage_three = (random.randint(5, 11)) * 1000


def start_pro_career():
    print("CHAPTER 1: The Choice")

    print(f"{name}, you have just finished a successful youth career at your\nlocal football club.")

    print("Alongside your talent, your agent has been very proactive\nand there are a number of clubs around Europe that would\nlike to sign you.")

    weekly_wage_club_one()

    print(f"""Three clubs have expressed their interest and they have guaranteed that you'll play at least 50% of the games in your first season. 
\nPlease see your options below:
\nOption 1: {CLUB_ONE[0]} for £{weekly_wage_one} per week
\nOption 2: {CLUB_ONE[1]} for £{weekly_wage_two} per week  
\nOption 3: {CLUB_ONE[2]} for £{weekly_wage_three} per week""")

    club_picked = ""
    while club_picked not in CLUB_ONE:
        club_picked = input("\nTo pick a team, please type one of the following: Benfica, Ajax or RB Salzburg\n")
        if club_picked.upper() == "BENFICA":
            print("You are heading to Lisbon, Portugal. Good luck in the upcoming season!")
            break
        elif club_picked.upper() == "AJAX":
            print("You are heading to Amsterdam, Netherlands. Good luck in the upcoming season!")
            break
        elif club_picked.upper() == "RB SALZBURG":
            print("You are heading to Salzburg, Austria. Good luck in the upcoming season!")
            break
        else:
            print("Invalid input, please select a club option from above!")


def club_one_end():
    global age
    age += 5

    print("Loading Chapter 2...")

    print("CHAPTER 2: A STAR IN THE MAKING")

    print("Five years later...")

    stat.club_one_stats()


def start_club_two():
    print("CHAPTER 3: BIG MONEY MOVE")

    transfer_fee = "£" + str(random.randint(55, 80)) + " Million"
    second_club = random.choice(CLUB_TWO)

    print(f"""You are currently preparing for a pre-season tour when you get a call from your agent. 
  
Your agent tells you that some big Premier League clubs are battling it out for your signature!

You've been told that your current club has accepted a fee of {transfer_fee} from {second_club}.""")

    global weekly_wage_one
    weekly_wage_one = "£" + str(random.randint(150, 200)) + "k"

    negotiated_salary = "£" + str(random.randint(150, 200)) + "k"

    response = ""
    while response not in YES_OR_NO:
        response = input(f"""{second_club} are offering you a weekly salary of {weekly_wage_one}.

Do you accept this offer or do you risk negotiating?
      
If you accept the offer type 'YES' if you want to negotiate type 'NO'""")

        if response.upper() == "NO":
            if negotiated_salary < weekly_wage_one:
                print(f"{second_club} are not impressed with the negotiations, so they have now offered you {negotiated_salary})")
                print(f"Congratulations {name}, you will now meeting up with your new teammates at {second_club}!")
                break
            elif negotiated_salary > weekly_wage_one:
                print(f"{second_club} are impressed by your negotiating skills, they have now offered {negotiated_salary}")
                print(f"Congratulations {name}, you will now meeting up with your new teammates at {second_club}!")
                break
            else:
                print(f"The offer stands at {weekly_wage_one}, {second_club} will not negotiate!")
                print(f"Congratulations {name}, you will now meeting up with your new teammates at {second_club}!")
        elif response.upper() == "YES":
            print(f"Congratulations {name}, you will now meeting up with your new teammates at {second_club}!")
            break
        else:
            print("Please type either yes or no.")


def at_club_two():
    print("CHAPTER 4: HIGH FLYER")

    sponsor = random.choice(SPONSORSHIP_DEAL)
    sponsor_salary = "£" + str(random.randint(1, 5)) + " Million"

    print(f"""Your big money move to has made headlines.
  
    {sponsor} has contacted you and would like to offer you a sponsorship
    deal worth {sponsor_salary} per year.""")

def main():
    introduction()

    start_club_two()

if __name__ == "__main__":
    main()