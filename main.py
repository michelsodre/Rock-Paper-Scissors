import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player} computer chose {computer}")
    if player == computer:
        return "Tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors, you win"
        else:
            return "Paper cover rock, you lose"
    elif player == "papper":
        if computer == "rock":
            return "Paper cover rock, you win"
        else:
            return "scissors cut papper, you lose"
    elif player == "scissors":
        if computer == "papper":
            return "scissors cut papper, you win"
        else:
            return "Rock smashes scissors, you lose"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
