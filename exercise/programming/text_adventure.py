import random
import re


# Simulating the flow of the game

# Player: Eren - human that can transform into a titan 40 HP and max damage of 5
# Enemy 1: Annie - female titan with 5 HP and a max damage of 2
# Enemy 2: Rainer - armoured titan with 10 HP and a max damage of 4
# Enemy 3: Berhold - giant titan with 20 HP and a max damage of 6

print("""Welcome to Attack on Titans. 
An attack defend/game based on Season 1 of the namesake anime. 
You will face three different titan opponents on your way to Shiganshina.
Each fight can take multiple rounds. Each round you get to decide whether to defend or attack.
If you attack, a certain amount of damage is dealt to your opponent.
Opponents attack every round as long as they are alive.
If you decide to defend, no damage is dealt to the opponent. 
Instead, the damage the opponent deals to the player is cut in half.

You and your opponents have a certain amount of health points (HP) represented as an integer. 
If the value drops below 0, the player or opponent is defeated.
The amount of damage a player or opponent deals is limited by a maximum damage per character.
When a player or opponent attacks, a random damage value is generated between 1 and the max damage.
The game is lost if the player dies. The game is won if all opponents have been defeated.
If you are ready to start type 'start'.
""")

user_start = input().lower

if user_start == 'start':
    print('''Ready for your first opponent? It is the female titan, Annie, that attacked the survey corps on their way to Shiganshina. 
    Are you going to "attack" or "defend" from Annie?''')
    user_input = input().lower()
    if user_input != 'attack' or user_input != 'defend':
        print("What you have entered is not a valid command. Please try again")
    
    while hp_titan >= 0 and hp_player >= 0:
        if user_input == 'attack':
            print(f"You just attacked the female titan and dealt {damage_dealt_player} and the female titan's HP is down to {hp_titan}")
            pass # damage will be a random number between 1 and 5
        elif user_input == 'defend':
            print (f"The female titan dealt a ferocious blow of {damage_dealt_titan} and your HP is down to {hp_player}")
            pass