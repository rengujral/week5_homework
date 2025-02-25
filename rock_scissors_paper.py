# prompt the user to enter the value R/S/P
# rock = 0 paper = 1 scissors= 2

import random
# function to request input from user
def get_user_choice():
    user_choice = input("Pick your choice from Rock, Paper, or Scissors by inputting either R, P, or S: ").upper()
    # the .upper Converts the player's input to uppercase to ensure case insensitivity.
    if user_choice == "P":
        print("Your choice: Paper")
        return "Paper"
    elif user_choice == "S":
        print("Your choice: Scissors")
        return "Scissors"
    elif user_choice == "R":
        print("Your choice: Rock")
        return "Rock"
    else:
        print("Please input either P, S, or R")


# function to termine the computer choice
def get_computer_choice() -> str:
    computer_choices = {0:"rock", 1:'paper', 2:'scissors'}
    # we create a list map the values
    return computer_choices[random.choice([0, 1, 2])]
# the function random.choice() from the module random returns a randomly selected value from the list[]


# function to define possible combinations
def winning_combinations(computer, user):
    if computer == user:
        return'it is a tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user== 'paper' and computer == 'rock'):
        return"You win!"
    else:
        return"You lose!"

# # dictionary defining winning key value pairs
#     winning_conditions = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
#
#     # if loop determining whether user beats computer or if there is a draw and displaying corresponding message
#     if player == computer:
#         return "It's draw!"
#     elif winning_conditions [player] == computer:
#         return "You win!"
#     else:
#         return "You lose.."

def play_game():
    user_turn= get_user_choice()
    computer_turn = get_computer_choice()


    print(f'the computer choice: {computer_turn}')

    result = winning_combinations(user_turn, computer_turn)
    print(result)

if __name__=='__main__':
    play_game()












