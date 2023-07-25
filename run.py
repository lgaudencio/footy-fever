
MAIN_MENU_OPTIONS = ["1", "2", "3"]

def introduction():
    print("Footy Fever")


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
        elif response == "2":
            print("Game instructions")
        elif response == "3":
            print("Starting Game...")
        else:
            print("Please enter a number between 1 and 3")