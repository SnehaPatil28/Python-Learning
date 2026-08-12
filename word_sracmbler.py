import random
print("Word Srambler 🎉")

words = ['python', 'game', 'learn', 'jump']

while True:
    original_word = random.choice(words)

    letter = list(original_word)
    random.shuffle(letter)
    srambled_word = "".join(letter)

    print("Srambled Word: ", srambled_word)

    guess = input("Guess Word? ").lower()

    if guess == original_word:
        print("Congrats!! 🎉")
    else:
        print("Wrong Guess 😒, original word is ", original_word)

    again = input("Try again? ").lower()

    if not again.startswith('y'):
        print("Goodbye!!")
        break
