print("GRADE CALCULATOR")
scores = []

while True:
    score = input("Enter a test score (or 'done'): ")
    if score.lower() == "done":
        print("👋 Goodbye")
        break

    scores.append(float(score))
    avg = sum(scores) / len(score)
    print(f"Average score: {avg: .1f}")
    if avg >= 90:
        print("Grade: A")
    elif avg >= 80:
        print("Grade: B")
    elif avg >= 70:
        print("Grade: C")
    else:
        print("Grade: F")
