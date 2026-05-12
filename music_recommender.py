import random

print("Music Recommender")

genres = {
    "rock": ["AC/DC", "Queens", "Led Zeppelin"],
    "pop": ["Taylor Swift", "Ed Sheeran", "Arina Grande"],
    "hip-hop": ["Kendrick Lamar", "Drake", "J. Cole"]
}

choice = input("What gener do you like? (rock/pop/hip-hop): ")

if choice not in genres:
    print("Sorry, I don't know that genre.")
else:
    print(f"Check out {random.choice(genres[choice])}")
