from rock_scissors_paper import play_game

# create while true infinite loop to loop through the game
while True:
    play_game()
    rps_loop = input("\nDo you want to play again? (yes/no)\n").strip()
    if rps_loop == "yes":
        print("Yay!")
    else:
        print("Okay, goodbye.")
        break