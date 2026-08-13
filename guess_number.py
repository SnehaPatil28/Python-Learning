import random

print("Guess The Number 🎉")

while True:
    number = random.choice(range(1, 101))
    i = 1
    while i <= 10:
        guess = int(input(f"Attempt {i}/10. Enter your guess: "))

        if guess > number:
            print("Too high!! Try lower number!")
            print(f"You have {10 - i} attempt left!")
            i += 1
        elif guess < number:
            print("Too low!! Try lower number!")
            print(f"You have {10 - i} attempt left!")
            i += 1
        else:
            print(
                f"Congratulation 🎉, You guessed number {number} in {i} attempt")
            break

    again = input("Wanna play again?").lower()

    if not again.startswith('y'):
        print("Goodbye!!")
        break
