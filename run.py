
MAIN_MENU_OPTIONS = ["1", "2", "3"]

name = ""

weekly_wage_one = ""
weekly_wage_two = ""
weekly_wage_three = ""

def introduction():
    print("Footy Fever")
    main_menu()
    input_name()


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


def main():
    introduction()

if __name__ == "__main__":
    main()