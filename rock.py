import random

def main():

    player_wins = 0
    computer_wins = 0
    ties = 0
    total_games = 0
    print("Welcome to ROCK, PAPER, and SCISSORS.")
    again = "y"
    while again == "y":
        play_games(ties,computer_wins, player_wins, total_games)
        again = input("Would you like to play?")
        if again != "y":
                accumulator(ties,computer_wins, player_wins,total_games)

def get_computers_choice():

    for count in range(1):
        computers_choice = random.randint(1,3)
    if computers_choice == 1:
        computers_choice = "ROCK"
    elif computers_choice == 2:
        computers_choice = "PAPER"
    else:
        computers_choice = "SCISSORS"
    return computers_choice

def get_players_choice():

    players_choice = input("Enter 1 for ROCK, 2 for PAPER, or 3 for SCISSORS: ")
    if players_choice == "1":
        players_choice = "ROCK"
    elif players_choice == "2":
        players_choice = "PAPER"
    elif players_choice == "3":
        players_choice = "SCISSORS"
    else:
        print("ERROR Choice must be 1 for ROCK, 2 for PAPER, or 3 for SCISSORS")
        get_players_choice()
    return players_choice
def play_games(ties,computer_wins, player_wins,total_games):

    computers_choice = get_computers_choice()
    players_choice = get_players_choice()
    if computers_choice == "ROCK":
        print("The computer's choice is ROCK.")
    elif computers_choice == "PAPER":
        print("The computer's choice is PAPER.")
    else:
        print("The computer's choice is SCISSORS.")
    winner = determine_the_winner(computers_choice, players_choice,computer_wins, player_wins, total_games, ties)
    return winner,ties,computer_wins, player_wins,total_games

def determine_the_winner(computers_choice, players_choice,ties,computer_wins,
 player_wins,total_games):

    if computers_choice == players_choice:
        print("Game is a tie.")
        ties = ties + 1
        total_games = total_games + 1
        return total_games, ties
    elif computers_choice == "ROCK" and players_choice == "SCISSORS":
        print("You lose, ROCK crushes SCISSORS.")
        computer_wins = computer_wins + 1
        total_games = total_games + 1
        return computer_wins, total_games
    elif computers_choice == "ROCK" and players_choice == "PAPER":
        print("You win, PAPER covers ROCK.")
        player_wins = player_wins + 1
        total_games = total_games + 1
        return player_wins, total_games
    elif computers_choice == "PAPER" and players_choice == "ROCK":
        print("You lose, PAPER covers ROCK.")
        computer_wins = computer_wins + 1
        total_games = total_games + 1
        return computer_wins, total_games
    elif computers_choice == "PAPER" and players_choice == "SCISSORS":
        print("You win, SCISSORS cuts PAPER.")
        player_wins = player_wins + 1
        total_games = total_games + 1
        return player_wins, total_games
    elif computers_choice == "SCISSORS" and players_choice == "PAPER":
        print("You lose, SCISSORS cuts PAPER.")
        computer_wins = computer_wins + 1
        total_games = total_games + 1
        return computer_wins, total_games
    elif computers_choice == "SCISSORS" and players_choice == "ROCK":
        print("You win, ROCK crushes SCISSORS.")
        player_wins = player_wins + 1
        total_games = total_games + 1
        return player_wins, total_games

def accumulator(ties,computer_wins, player_wins,total_games):

    print("You have played", total_games, "games")
    print("You won", player_wins, "games")
    print("You lost", computer_wins, "games")
    print("You tied", ties, "games")

main()