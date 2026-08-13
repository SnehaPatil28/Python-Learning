from time import sleep

print("CountDown Timer!!")

while True:
    seconds = int(input("Enter seconds to countdown from: "))

    while seconds > 0:
        print(f"{seconds} seconds remaining...")
        seconds -= 1
        sleep(1)
    print("CountDown Complete!! 🎉")
    again = input("Start another countdown?").lower()

    if not again.startswith('y'):
        print("Goodbye!!")
        break
