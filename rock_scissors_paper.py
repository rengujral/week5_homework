# prompt the user to enter the value R/S/P
# rock = 0 paper = 1 scissors= 2

import random
# function to request input from user
def get_user_choice():
    user_choice = input('Enter your choice (rock, paper, scissors): ')
    return user_choice


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

def play_game():
    user_turn= get_user_choice()
    computer_turn = get_computer_choice()

    print(f'user choice:{user_turn}')
    print(f'the computer choice: {computer_turn}')

    result = winning_combinations(user_turn, computer_turn)
    print(result)

if __name__=='__main__':
    play_game()












