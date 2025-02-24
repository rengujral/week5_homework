# import random to be able to randomise the computer's weapon choice
import random

# define function user_choice to determine user's choice
def user_choice():
    """Prompts the user to choose between Rock, Paper and Scissors and initiates the game."""
    # prompt the user to enter the initial of the weapon of their choice
    user_input = input("Enter R for Rock, P for Paper, S for Scissors:\n").strip().upper()

    # Dictionary with user input as keys to full names as values pairs
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    # if loop determining if user input is valid
    if user_input in choices:
        # if valid it displays the full name of the input
        return choices[user_input]
    else:
        # else it states that the input is invalid and prompts the user to enter a choice again
        print("Invalid Choice! Please enter one of the three choices above!")
        return user_choice()

# define function computer_choice to determine computer's choice
def computer_choice():
    """Determines the computer's choice of weapon from Rock, Paper and Scissors."""
    choices = ['Rock', 'Paper', 'Scissors']
    # uses the random function to pick a random choice
    return random.choice(choices)

# define function choose_winner to determine the winner
def choose_winner(player, computer):
    """Determines the winner between the computer and user."""

    # dictionary defining winning key value pairs
    winning_conditions = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

    # if loop determining whether user beats computer or if there is a draw and displaying corresponding message
    if player == computer:
        return "It's draw!"
    elif winning_conditions [player] == computer:
        return "You win!"
    else:
        return "You lose.."

# function created to play the game
def play_game():
    """Runs the Rock, Paper, Scissors game."""
    # user input versus computer choice
    your_attack = user_choice()
    computer_attack = computer_choice()


    # Display choices
    print(f"\nYou chose: {your_attack}")
    print(f"Computer chose: {computer_attack}")

# Determine and print the winner
    result = choose_winner(your_attack, computer_attack)
    print(result)

if __name__ == "__main__":
    play_game()