print("CHARACTER TYPE CHECKER")

text = input("Enter a single character: ")

if text.isdigit():
    print("This is a number.")
elif text.isalpha():
    print("This is a letter.")
else:
    print("This is a special character.")
