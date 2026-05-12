import random
print("Word Scarmbler")

while True:
    word = input("Enter a word to scramble (or quit): ")

    if word.lower() == 'quit':
        print("Goodbye👋")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrabled: {"".join(letters)}")
