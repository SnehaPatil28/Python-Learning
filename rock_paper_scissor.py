import random
import time

game = ["rock", "paper", "scissor"]

rounds = 1
score_you = 0
score_computer = 0

while True:

    while rounds < 4:
        player_guess = input(
            "Enter your choice (rock/paper/scissor): "
        ).lower()

        if player_guess not in game:
            print("Invalid choice! Please choose rock, paper, or scissor.")
            continue

        print(f"You choose {player_guess}")
        print("Let computer choose....")
        time.sleep(1)

        computer_guess = random.choice(game)
        print(f"Computer choose {computer_guess}")

        if player_guess == computer_guess:
            print("It's a tie!")

        elif (
            (player_guess == "rock" and computer_guess == "scissor")
            or (player_guess == "paper" and computer_guess == "rock")
            or (player_guess == "scissor" and computer_guess == "paper")
        ):
            print("You won this round!!")
            score_you += 1

        else:
            print("Computer won this round!")
            score_computer += 1

        rounds += 1

    if score_you > score_computer:
        print("You are the winner 🎉")
    elif score_computer > score_you:
        print("You lost this game 😭")
    else:
        print("The game is a tie! 🤝")

    play_again = input("Play Again? ").lower()

    if play_again.startswith("y"):
        rounds = 1
        score_computer = 0
        score_you = 0
        continue
    else:
        print("GoodBYEE!!!")
        break
