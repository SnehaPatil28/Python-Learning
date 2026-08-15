# 🐍 Basic Python & Games

A collection of beginner-friendly Python scripts covering core concepts and fun mini-games. Great for anyone learning Python fundamentals.

---

## 📁 Project Structure

```
├── Basics/
│   └── Variables.py        # Python variables, data types, and string methods
├── check_char_type.py      # Checks if input is a letter, number, or special character
├── coin_flip_game.py       # Guess heads or tails in a coin flip game
├── color_mixer.py          # Mix two colors and see the result
├── counter.py              # Countdown timer
├── grade_calculator.py     # Calculate average score and letter grade
├── guess_number.py         # Guess the random number in 10 attempts
├── memory_sequence.py      # Remember and repeat a growing number sequence
├── music_recommender.py    # Get an artist recommendation based on your genre
├── name_generator.py       # Generate random fantasy names
├── step_counter.py         # Track your daily step goal
├── text_formatter.py       # Format text to upper, lower, title, or sentence case
├── vowel_counter.py        # Count vowels in any text
├── website_checker.py      # Check if a URL uses HTTP or HTTPS
├── word_game.py            # Respond with related words against the clock
└── word_sracmbler.py       # Unscramble a shuffled word
```

---

## 📚 Basics

### `Basics/Variables.py`
Covers Python fundamentals: variables, data types (`str`, `int`, `float`, `bool`), f-strings, string slicing, and common string methods like `.upper()`, `.lower()`, `.replace()`.

---

## 🎮 Games

### `coin_flip_game.py`
Guess **heads** or **tails** before a coin is flipped. Play as many rounds as you like.

### `guess_number.py`
A random number between 1–100 is chosen. You have **10 attempts** to guess it, with higher/lower hints after each guess.

### `memory_sequence.py`
A sequence of numbers is flashed on screen one at a time. Type them back in order. Each round adds one more number — see how far you can go!

### `word_game.py`
A prompt word appears and you type a related word as fast as you can. Points are awarded based on response time.

### `word_sracmbler.py`
A word is scrambled and you have to guess the original. A classic unscramble challenge.

### `color_mixer.py`
Enter two colors and the mixer tells you what color they make together (e.g. red + blue = purple).

---

## 🛠️ Utilities

### `check_char_type.py`
Enter a single character and it tells you whether it's a **letter**, **number**, or **special character**.

### `counter.py`
A simple **countdown timer** — enter any number of seconds and watch it count down.

### `grade_calculator.py`
Enter test scores one by one. The script calculates the running average and assigns a letter grade (A, B, C, or F).

### `music_recommender.py`
Pick a genre (**rock**, **pop**, or **hip-hop**) and get a random artist recommendation.

### `name_generator.py`
Generates random **fantasy names** by combining fun first and last name parts.

### `step_counter.py`
Enter your daily step goal and how many steps you've taken — it tells you how many more you need.

### `text_formatter.py`
Format any text to one of four styles: **UPPER CASE**, **lower case**, **Title Case**, or **Sentence case**.

### `vowel_counter.py`
Enter any text and it counts the total number of vowels (a, e, i, o, u).

### `website_checker.py`
Enter a URL and it checks whether the site uses **HTTPS** (secure) or **HTTP** (not secure).

---

## 🚀 Getting Started

You only need Python 3 installed. No external packages required.

```bash
python <script_name>.py
```

For example:

```bash
python guess_number.py
```

---

## 🧰 Requirements

- Python 3.x
- No third-party libraries — only built-in modules (`random`, `time`, `os`, `math`)
