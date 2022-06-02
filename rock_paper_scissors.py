"""
input - R, P, S - Human
random library - Computer

"""
import random


winner_name = ""
options_list = ["R", "P", "S"]

while True:
    # Human
    while True:
        print("Press R for Rock")
        print("Press P for Paper")
        print("Press S for Scissors")
        human_choice = input("Option: ")
        print(f"Human Choice: {human_choice}")

        # checking for invalid human input
        if human_choice not in options_list:
            print(f"Invalid input: {human_choice}, please enter the option")
        else:
            break

    # Computer
    computer_choice = random.choice(options_list)
    print(f"Computer Choice: {computer_choice}")

    # assingning index to our players with dictionary so we can reuse later
    players = {0: "CPU", 1: "Human"}
    all_choices = [computer_choice, human_choice]

    # rules for picking winner
    if "R" in all_choices and "S" in all_choices:
        winner_index = all_choices.index("R")
        winner_name = players[winner_index]
        print("Rock beats Scissors")
        print(f"{winner_name} wins!")
        break

    elif "P" in all_choices and "R" in all_choices:
        winner_index = all_choices.index("P")
        winner_name = players[winner_index]
        print("Paper beats Scissors")
        print(f"{winner_name} wins!")
        break

    elif "S" in all_choices and "P" in all_choices:
        winner_index = all_choices.index("S")
        winner_name = players[winner_index]
        print("Scissors beats Paper")
        print(f"{winner_name} wins!")
        break
    else:
        print()
        print("No winner, retrying...")
        print()
        print()
