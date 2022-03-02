import random

jokes_responses = {
    "country":[
        "What's the best thing about Switzerland? Don't know, but the flag is a big plus"
        ],
    "acting": [
        "Why do we tell actors to break a leg? Because every play has a cast."
        ],
    "animals": [
        "What do you call a parade of rabbits hopping backwards? A receding hare-line.", 
        "What do you call a magic dog? A labracadabrador." 
        ],
    "anatomy":[
        "What did the left eye say to the right eye? Between you and me something smells."
    ],
    "cooking":[
        "What do you call a fake noodle? An impasta!"
        ],
    "math":[
        "What did the 0 say to the 8? Nice belt!"
        ],
    "pirates": [
        "What did the pirate say when he turned 80? Aye matey."
        ],
    "astronauts": [
        "What is an astronaut's favourite part on a computer? The space bar."
        ],
    "hipster": [
        "Why did the hipster burn his mouth? He drank the coffee before it was cool.",
        "How do you drown a hipster? You throw them in the mainstream."
        ],
    "batman": [
        "Where does Batman go to the bathroom? The batroom."
        ],
    "daily": [
        "Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, 'What's the word on the street?'"
        ],
    "karma": [
        "Hear about the new restaurant called Karma? There's no menu: You get what you deserve."
        ],
    "science": [
        "Why don't scientists trust atoms? Because they make up everything"
        ],
    "default": [
        "How do you count cows? With a cow-culator."
        ]
}


def response(user_command):
    if user_command == 'all':
        for joke_bot_message in jokes_responses.values():
            return joke_bot_message
    elif user_command == 'random':
        for joke_bot_message in jokes_responses.values():
            return random.choice(joke_bot_message)
    elif user_command in jokes_responses:
        joke_bot_message = random.choice(jokes_responses[user_command])
    else:
        joke_bot_message = random.choice(jokes_responses["default"])
    return joke_bot_message

def related(user_text):
    if "all" in user_text:
        user_text_new = "all"
    elif "acting" in user_text:
        user_text_new = "acting"
    elif "anatomy" in user_text:
        user_text_new = "anatomy"
    elif "astronauts" in user_text:
        user_text_new = "astronauts"
    elif "batman" in user_text:
        user_text_new = "batman"
    elif "cooking" in user_text:
        user_text_new = "cooking"
    elif "country" in user_text:
        user_text_new = "country"
    elif "daily" in user_text:
        user_text_new = "daily"
    elif "hipster" in user_text:
        user_text_new = "hipster"
    elif "karma" in user_text:
        user_text_new = "karma"
    elif "math" in user_text:
        user_text_new = "math"
    elif "pirates" in user_text:
        user_text_new = "pirates"
    elif "random" in user_text:
        user_text_new = "random"
    elif "science" in user_text:
        user_text_new = "science"
    return user_text_new

print("""
Joke Bot: Hello there! 
Please enter "all" if you want all jokes to be displayed,
"random" for a random joke or one of the following categories for a more specific joke: 
acting, anatomy, animals, astronauts, batman, cooking, country, daily, hipster, karma, math, pirates, science .
\nYou:""")
user_command = str(input()).lower()
user_text = related(user_command)

print(response(user_text))

