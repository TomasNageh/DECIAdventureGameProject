import time
import random


def print_pause(message, color=None):
    if color == "red":
        print(f"\033[91m{message}\033[0m")  # Print in red color
    elif color == "blue":
        print(f"\033[94m{message}\033[0m")  # Print in blue color
    else:
        print(message)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("To your left is a mysterious forest.")
    print_pause("In your hand, you hold your trusty (but not very "
                "effective) dagger.")
    print_pause("The game ends when you reach the following goal:")
    print_pause("The goal is to defeat the wicked fairy and achieve a "
                "score of 10 or higher.")


def get_input(message, options):
    while True:
        choice = input(message)
        if choice in options:
            return choice
        else:
            print_pause("Please enter a valid input.")


def update_score(value):
    global score
    score += value
    print_pause(f"The current score is: {score}")
    if score >= 10:
        print_pause("Congratulations! You have achieved the goal.")
        print_pause("You successfully defeat the wicked fairy and win "
                    "the game.")
        print_pause("Thanks for playing! Goodbye!")
        quit()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                "steps a wicked fairy.")
    print_pause("Eep! This is the wicked fairy's house!")
    print_pause("The wicked fairy says, 'Who dares to disturb my "
                "peace?'")
    response = get_input("Enter 1 to apologize.\n"
                         "Enter 2 to challenge the wicked fairy.\n"
                         "What is your choice? (Please enter 1 or 2): ",
                         ["1", "2"])

    if response == "1":
        print_pause("You apologize to the wicked fairy for the "
                    "intrusion.")
        print_pause("The wicked fairy accepts your apology and rewards "
                    "you.")
        update_score(2)
    else:
        print_pause("You draw your dagger and prepare to fight.")
        if random.random() < 0.5:
            print_pause("You successfully defeat the wicked fairy!",
                        color="blue")
            update_score(3)
        else:
            print_pause("The wicked fairy overpowers you.")
            print_pause("You have been defeated!", color="red")
            update_score(-1)


def cave():
    print_pause("You peer cautiously into the cave.")
    if random.random() < 0.5:
        print_pause("You enter the cave and discover a friendly "
                    "creature.")
        print_pause("The friendly creature says, 'Greetings, "
                    "traveler!'")
        response = get_input("Enter 1 to chat with the creature.\n"
                             "Enter 2 to ask for its assistance.\n"
                             "What is your choice? (Please enter 1 or "
                             "2): ",
                             ["1", "2"])

        if response == "1":
            print_pause("You engage in a friendly conversation with the "
                        "creature.")
            print_pause("The creature shares some helpful advice.")
            update_score(1)
        else:
            print_pause("You ask the creature for help.")
            print_pause("The creature provides you with a magical "
                        "amulet.")
            update_score(2)
    else:
        print_pause("You enter the cave and encounter a fearsome "
                    "monster.")
        print_pause("The monster growls menacingly.")
        response = get_input("Enter 1 to fight the monster.\n"
                             "Enter 2 to try and sneak past it.\n"
                             "What is your choice? (Please enter 1 or "
                             "2): ",
                             ["1", "2"])

        if response == "1":
            if random.random() < 0.8:
                print_pause("You bravely fight the monster and defeat "
                            "it!")
                update_score(3)
            else:
                print_pause("The monster proves to be too powerful.")
                print_pause("You have been defeated!", color="red")
                update_score(-1)
        else:
            print_pause("You attempt to quietly sneak past the monster.")
            if random.random() < 0.7:
                print_pause("Your stealth skills succeed, and you bypass "
                            "the monster.")
                update_score(2)
            else:
                print_pause("The monster spots you and attacks!")
                print_pause("You have been defeated!", color="red")
                update_score(-1)


def forest():
    print_pause("You venture into the mysterious forest.")
    print_pause("As you make your way through the trees, you stumble "
                "upon a hidden treasure chest.")
    print_pause("You open the treasure chest and discover a valuable "
                "artifact!")
    update_score(2)


def play_game():
    intro()

    while True:
        print_pause("What would you like to do?")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("Enter 3 to venture into the forest.")
        print_pause("Enter 4 to check your score.")
        print_pause("Enter 5 to quit the game.")

        choice = get_input("What is your choice? (Please enter a "
                           "number): ",
                           ["1", "2", "3", "4", "5"])

        if choice == "1":
            house()
        elif choice == "2":
            cave()
        elif choice == "3":
            forest()
        elif choice == "4":
            print_pause(f"Your current score is: {score}")
        elif choice == "5":
            print_pause("Thanks for playing! Goodbye!")
            quit()

        print_pause("Would you like to continue exploring?")

        if get_input("Enter 'y' to continue exploring or 'n' to quit: ",
                     ["y", "n"]) == "n":
            print_pause("Thanks for playing! Goodbye!")
            quit()


score = 0
play_game()
