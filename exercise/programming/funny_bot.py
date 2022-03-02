import random;

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


def response(user_com):
    if user_com == 'all':
        for joke in jokes_responses.values():
            for joke_bot_message in joke:
                print(joke_bot_message)
    elif user_com == 'random':
        joke_bot_message = []
        for joke in jokes_responses.values():
            joke_bot_message.append(joke)
        print(random.choice(joke_bot_message))
    elif user_com in jokes_responses:
        joke_bot_message = random.choice(jokes_responses[user_com])
        return joke_bot_message
    else:
        print('One last one for the road:')
        joke_bot_message = jokes_responses["default"]
        return joke_bot_message


def related(user_text):
    if "all" in user_text:
        user_text_n = "all"
        return user_text_n
    elif "acting" in user_text:
        user_text_n = "acting"
        return user_text_n
    elif "anatomy" in user_text:
        user_text_n = "anatomy"
        return user_text_n
    elif "astronauts" in user_text:
        user_text_n = "astronauts"
        return user_text_n
    elif "batman" in user_text:
        user_text_n = "batman"
        return user_text_n
    elif "cooking" in user_text:
        user_text_n = "cooking"
        return user_text_n
    elif "country" in user_text:
        user_text_n = "country"
        return user_text_n
    elif "daily" in user_text:
        user_text_n = "daily"
        return user_text_n
    elif "hipster" in user_text:
        user_text_n = "hipster"
        return user_text_n
    elif "karma" in user_text:
        user_text_n = "karma"
        return user_text_n
    elif "math" in user_text:
        user_text_n = "math"
        return user_text_n
    elif "pirates" in user_text:
        user_text_n = "pirates"
        return user_text_n
    elif "random" in user_text:
        user_text_n = "random"
        return user_text_n
    elif "science" in user_text:
        user_text_n = "science"
        return user_text_n
    else:
        user_text_n = ""
        return user_text_n


while True:
    print("""
    Joke Bot: Hello! 

    Please enter "all" if you want all jokes to be displayed,
    "random" for a random joke or one of the following categories for a more specific joke: 
    acting, anatomy, animals, astronauts, batman, cooking, country, daily, hipster, karma, math, pirates, science .
    If you want to stop then please enter "exit" or "stop".
    \nYou:""")
    user_command = str(input()).lower()
    user_text = related(user_command)

    print(response(user_text))
    if user_command =="exit" or user_command == "stop":
        break

