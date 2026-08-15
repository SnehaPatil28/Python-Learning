import time, random

word_pairs = {
  "sky" : ["blue", "cloud", "bird", "fly", "sun"],
  "food" : ["eat", "cook", "tasty", "meal", "resturant"],
  "water" : ["drink", "ocean", "swim", "fish","boat"],
  "music" : ["song", "dance", "listen", "band"],
  "book" :["read", "story", "page", "author"]
}

print("Word Game")
print("Respond with a related word quickly")

score = 0
rounds = 0

while True:
  prompt = random.choice(list(word_pairs.keys()))
  related_words = word_pairs[prompt]

  print("\n Prompt word: ",prompt.upper())
  print("Quike! Type a word related to this prompt")

  start_time = time.time()

  response = input("> ").lower().strip()

  response_time = time.time() - start_time

  print("response time", response_time)

  if response in related_words:
    points = max(1, 5 - int(response_time))
    score += points
    print(f"Good association! +{points} points (answered in {response_time:.1f}s)")
  else:
    print(f"Not a common association. Related word includes: {' '.join(related_words)}")

  rounds += 1

  again = input("Wanna play again?").lower()

  if not again.startswith('y'):
    print("Goodbye!!")
    break



