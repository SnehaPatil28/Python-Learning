def count_word(text):
    return len(text.split())


def count_char(text, include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))


def sentence_count(text):
    ending = ["?", "!", "."]
    count = 0

    for char in text:
        if char in ending:
            count += 1

    if count == 0:
        return 1 if text.strip() else 0

    return count


def word_analysis(text):
    words = count_word(text)
    char_with_space = count_char(text, True)
    char_without_space = count_char(text, False)
    count_sentence = sentence_count(text)

    if count_sentence > 0:
        word_per_sentence = words / count_sentence
    else:
        word_per_sentence = 0

    if words > 0:
        chars_per_count = char_with_space / words
    else:
        chars_per_count = 0

    print("\nWord Analysis!!")
    print()
    print(f"Word count: {words}")
    print(f"Character with spaces: {char_with_space}")
    print(f"Character without spaces: {char_without_space}")
    print(f"Sentence count: {count_sentence}")
    print(f"Average word per sentence: {word_per_sentence:.1f}")
    print(f"Average character per word: {chars_per_count:.1f}")

    read_time_min = words / 255
    read_time_sec = read_time_min * 60

    if read_time_min < 1:
        print(f"Estimated reading time: {read_time_sec:.1f} seconds")
    else:
        print(f"Estimated reading time: {read_time_min:.1f} minutes")


def main():
    print("Word Analysis!!")

    while True:
        print("""Choose an option:

    1. Enter Text to analyze
    2. Exit
    """)

        choice = int(input("Your option: "))

        if choice == 1:
            print("Enter text below (press enter twice to finish):")
            lines = []

            while True:
                line = input()

                if not line:
                    break

                lines.append(line)

            text = "\n".join(lines)

            if not text.split():
                print("No text entered!!")
                continue

            word_analysis(text)

        elif choice == 2:
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


main()