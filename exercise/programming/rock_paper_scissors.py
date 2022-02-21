## importing the random package
import random

user_input = str(input('Want to play a game? Please type rock, paper, scissors:\n'))

moves = ["rock", "paper", "scissors"]
computer_moves = random.choice(moves)

print(f"The machine chose: {computer_moves}")

if user_input == computer_moves:
    print("It's a tie habib:t:i:s")
elif user_input == "rock":
    if computer_moves == "scissors":
        print("Rock beats scissors. You win, habib:t:i!")
    else:
        print("Paper beats the mighty rock. You loose, habiiiib:t:i!")
