## importing the random package
import random

# game start function
def game_start(user_game_start_input, rand):
    print(f'The machine chose {rand}')

    if user_game_start_input == rand:
        print("It's a tie, habib:t:i!")
    elif user_game_start_input <= rand:
        print("The machines have won, muhahaha. Now cry, habib:t:i!")
    elif user_game_start_input >= rand:
        print("Yalla habib:t:i. You win!")
    else:
        print("Something went terribly wrong")

# game end function
def game_end(user_continuation_input):
    if user_continuation_input == 'No' or user_continuation_input == 'no' or user_continuation_input == 'NO':
        return False
    else:
        return True

while True:

    user_game_start_input = int(input('To start the game please enter a number from 1 to 100 \n'))
    
    if user_game_start_input >= 101 or user_game_start_input <= 0:
        print('Ooopsi dasy, seems like your number is not between 1 and 100. Please try again.')
    else:
        rand = int(random.random()*100)
    
        game_start(user_game_start_input, rand)

        user_continuation_input = input('You want to keep going? [Yes/No]\n')

        if game_end(user_continuation_input) == False:
            break
        else:
            continue

