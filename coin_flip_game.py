import random

print("Coin Flip Game\nGuess heads or tails!")

while True:
    choise = input("Enter your guess (head/tails): ")

    if choise.lower() == random.choice(['head', 'tails']):
        print("You guessed correctly! You win!🎉"),
    else:
        print("Sorry, wrong guess. Try again!")

    repeat = input("Play again (yes/no): ")
    if repeat == 'no' or 'n':
        print("Thank you for playing!")
        break
