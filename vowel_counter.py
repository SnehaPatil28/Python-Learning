print("Vowel Counter")

while True:
    text = input("Enter the text (or quit): ")

    if text.lower() == 'quit':
        break

    count = 0
    letters = list(text.lower())
    print(letters)
    for i in letters:
        if i in ['a', 'e', 'o', 'i', 'u']:
            count += 1

    print(f"Tat text has {count} vowels")


# vowels = sum(1 for char in text.lower() if char in "aeiou")
# print(vowels)
