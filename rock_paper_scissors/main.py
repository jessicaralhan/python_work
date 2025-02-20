import random 

def get_choices():
    player_choice = input("enter player's choice-")
    options = ["rock", "paper", "scissors"]
    computer_choice = input("enter computer's choice-")
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"your choice {player}, computer choice {computer}")
    if player == computer:
        print("its a tie")
    elif player == "rock":
        if computer == "scissor":
            print("rock smashes scissor ")
    else:
        print("paper covers rock")

check_win("rock", "paper")
