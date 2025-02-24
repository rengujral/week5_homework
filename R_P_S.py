import random
# Importing the random module to enable the computer to make a random choice.

def players_weapon():
    """Gets the player's weapon choice and returns the full name."""
    # Prompting the player to choose Rock, Paper, or Scissors using shorthand (R, P, S).
    player_weapon = input("Pick your weapon from Rock, Paper, or Scissors by inputting either R, P, or S: ").upper()
    # the .upper Converts the player's input to uppercase to ensure case insensitivity.
    if player_weapon == "P":
        print("Your weapon is: Paper")
        return "Paper"
    elif player_weapon == "S":
        print("Your weapon is: Scissors")
        return "Scissors"
    elif player_weapon == "R":
        print("Your weapon is: Rock")
        return "Rock"
    else:
        print("Please input either P, S, or R")
        return players_weapon()


def computers_weapon():
    """Randomly selects a weapon for the computer and returns it."""
    weapons = ["Rock", "Paper", "Scissors"]
    # List of available weapon choices.
    computer_weapon = random.choice(weapons)
    # Using `random.choice(weapons)` to randomly pick one item from the list.
    # This means that each time the function is called, the computer selects one of the three options at random.
    print(f"The computer's weapon is: {computer_weapon}")
    return computer_weapon
 # Returning the computer's randomly selected weapon so it can be used in the winner determination function.


def winner(player, computer):
    """Determines the winner based on the player's and computer's choices."""
    # If the player's choice and the computer's choice are the same, it's a draw.
    if player == computer:
        print("It's a draw!")
    elif (player == "Rock" and computer == "Scissors") or \
            (player == "Paper" and computer == "Rock") or \
            (player == "Scissors" and computer == "Paper"):
        print("You win!")
    else:
        print("The computer wins!")
 # If the player did not win and it's not a draw, the computer wins by default.

# Running the game
player_choice = players_weapon()
# Calling `players_weapon()` to get the player's chosen weapon and storing it in `player_choice`.
computer_choice = computers_weapon()
# Calling `computers_weapon()` to get the computer's randomly chosen weapon and storing it in `computer_choice`.
winner(player_choice, computer_choice)
# Calling the `winner()` function with both player and computer choices to determine and display the winner.
