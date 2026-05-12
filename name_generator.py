import random
print("Fantasy Name Generator")

first = ["sky", "Star",
         "Sun", "Moon", "Fire", "Ice"]

last = ["rider", "walker", "hunter", "seeker", "dancer"]

count = int(input("How many names do you want? "))

for i in range(count):
    first_name = random.choice(first)
    last_name = random.choice(last)
    print(first_name+last_name)
