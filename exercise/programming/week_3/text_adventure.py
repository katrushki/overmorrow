import random


# Setting the flow of the game

# Player and Titan class
# Player: Eren - human that can transform into a titan 40 HP and max damage of 5
class Player:
    def __init__(self, hp, maxD, name):
        self.hp = hp
        self.maxD = random.randint(1, maxD)
        self.name = name

    def description(self):
        print(f"{self.name} is the player in this game!")

player = Player(40, 5, 'Eren Jäger')

class Titan:
    def __init__(self, hp, maxD, name):
        self.hp = hp
        self.maxD = random.randint(1, maxD)
        self.name = name

    def description(self):
        print(f"{self.name} the titan is your opponent. She has {self.hp} HP and can deal {self.maxD} damage.")

# Enemy 1: Annie - female titan with 5 HP and a max damage of 2
annie_titan = Titan(5,2,'Annie')
# Enemy 2: Rainer - armoured titan with 10 HP and a max damage of 4
rainer_titan = Titan(10, 4, 'Rainer')
# Enemy 3: Berhold - giant titan with 20 HP and a max damage of 6
berthold_titan = Titan(20, 6, 'Berthold')

def help():
    print("""You can use the following commands: \n
    'attack': attacks the enemy
    'defend': defends an attack and halves the damage
    """)

def typo(type):
    type_error = ["Nope that won't work", "Please try again", "There seems to be a type. Try again, please.", "I did not quite catch that. Could you try again?"]

    if type == 'typo':
        error = random.choice(type_error)

    print(error)

def game(player, titan):
    while player.hp >=0 and titan.hp >=0:
        game_turn = 'player'
        player_defend = False
        titan_is_dead = False


        while game_turn == 'player':
            game_input = input(f'''
            Ready for your  opponent? It is the titan, {titan.name}, that attacked the survey corps on their way to Shiganshina. 
            Are you going to "attack" or "defend" from {titan.name}?''')
            
            if game_input == 'help':
                help()
                continue

            elif game_input == 'attack':
                player_damage = player.maxD
                titan.hp -= player_damage
                print(f"\nYou just attacked {titan.name} and dealt {player_damage} damage! {titan.name} has {titan.hp} HP left")
                game_turn = 'titan'

            elif game_input == 'defend':
                titan_damage = titan.maxD /2
                player.hp -= titan_damage
                player_defend = True
                game_turn = 'titan'


            elif game_input == 'quit':
                break

            else:
                typo('typo')
                continue

        if player.hp <= 0:
            print("You've been bested. The game is over. Humankind is lost.")
            break

        elif titan.hp <= 0:
            print(f"You have won against {titan.name} the titan! Hurray!")
            titan_is_dead = True
            break

        elif titan_is_dead == False:

            while game_turn == 'titan':
                if player_defend == False:
                    titan_damage = titan.maxD
                else:
                    titan_damage = titan.maxD / 2
                player.hp -= titan_damage

                message_titan = str(titan_damage)
                message_player = str(player.hp)
                print(f"The monster did {message_titan} damage! You have {message_player} HP left.")
                game_turn = 'player'


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

user_start = input()

if user_start == 'start':
    game(player, annie_titan)
else:
    print('I am sorry, this command does not work. Please enter "start" to begin.')

print("""It is time for round number two""")

game(player, rainer_titan)

print("""It is time for round number three""")

game(player, berthold_titan)