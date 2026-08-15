import time
import random
import os


def clear_screen():
    """clear the terminal scrren"""
    os.system("cls" if os.name == "nt" else "clear")


print("Memory Sequence Game")
print("Remember the sequence and type it back")

input("Press enter to start...")

sequence = []
curr_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screen()

    print("Round ", curr_round)
    print(f"Remember this sequence of {len(sequence)} numbers: ")

    for number in sequence:
        time.sleep(0.7)
        print(number)
        time.sleep(0.7)
        clear_screen()

    print("Now repeat the sequence: ")
    player_ans = input("> ")

    try:
        player_sequence = [int(num) for num in player_ans.split()]

    except ValueError:
        print("Please enter numbers only!!")
        game_over = True
        continue

    if player_sequence == sequence:
        print("Congrates!!!!")
        curr_round += 1
        time.sleep(2)
    else:
        print(f"Game over! You remembered all {curr_round - 1} numbers")
        print(f"Correct sequence: {' '.join(str(num) for num in sequence)}")
        game_over = True

    if game_over:
        play_again = input("Play again?").lower()
        if play_again.startswith('y'):
            sequence = []
            curr_round = 1
            game_over = False
        else:
            print("Thanks")
