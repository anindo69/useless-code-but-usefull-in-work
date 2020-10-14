
import random
import sys

choices = ["rock", "paper", "scissors"]

def check_victory(computer_choice, user_choice):
    if user_choice == computer_choice:
        return "tie"
    elif computer_choice == "rock" and user_choice == "paper":
        return "won"
    elif computer_choice == "paper" and user_choice == "scissors":
        return "won"
    elif computer_choice == "scissors" and user_choice == "rock":
        return "won"
    else:
        return "lost"


def play():
    # get input from user
    user_choice = None
    while user_choice not in choices:
        user_choice = input("Enter your choice: ")
        # check if user wants to quit
        if user_choice == "quit":
            sys.exit()

    computer_choice = random.choice(choices)

    # output result
    print(f"Computer choose: {computer_choice}")
    print("You " + check_victory(computer_choice, user_choice), end="\n\n")


if __name__ == "__main__":
    while True:
        play()