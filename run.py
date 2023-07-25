import random

MAIN_MENU_OPTIONS = ["1", "2", "3"]
CLUB_ONE = ["BENFICA", "AJAX", "RB SALZBURG"]

name = ""

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


def main():
    introduction()

if __name__ == "__main__":
    main()