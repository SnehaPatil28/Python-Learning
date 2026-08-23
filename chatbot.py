import random
import time


def chatbot():

    greetings = ["Hello there!", "Hi friend!",
                 "Hey! nice to meet you!", "Howdy!"]
    farewells = ["Goodbye!", "See you later!", "Bye bye!"]
    jokes = ["Why don't scientist trust atoms? Bcz they make up everything",
             "What do you call a fake noodle? An impasta!!",
             "Why did the scarecrow win an award? Bcz he was outstanding!",
             "What do you call a bear with no teeth? A gummy bear"]
    bot_name = "ChatBot"
    print(f"{chatbot} is starting up...")
    time.sleep(1)
    print(f"Welcome to {bot_name}!")

    print("I can chat about:\n")
    print("'Joke' - Hear a funny Joke\n"
          "'Color' - My favorite color"
          "'Bye' - End our chat")
    time.sleep(1)

    chating = True
    user_name = input("What's your name?").strip()
    print(f"{bot_name}: Nice to meet you, {user_name}! How can I help you?")

    while chating:
        user_in = input("You: ").strip().lower()

        if user_in in ["hi", "hello", "hey", "howdy"]:
            print(f"{bot_name}: {random.choice(greetings)}")

        elif "joke" in user_in:
            print(f"{bot_name}: {random.choice(jokes)}")

        elif "color" in user_in:
            print(f"{bot_name}: My favorite color is blue! What's yours?")
            color = input("You: ").strip()
            print(f"{bot_name}: {color} is a great color")

        elif user_in in ["bye", "goodbye", "exit", "quite"]:
            print(f"{bot_name}: {random.choice(farewells)}")
            print(f"{bot_name}: It was fun chatting with you, {user_name}.")
            chating = False

        else:
            print(f"{bot_name}: I'm not sure about what are you talking?")

    print("Thanks for chatting")


chatbot()
