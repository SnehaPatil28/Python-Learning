print("📢TEXT CAPITALIZER")

text = input("Enter the text: ")

print("1. Upper case \n2. Lower case \n3. Title case \n4. Sentence case")

choise = int(input("Choose a format (1-4):"))

match choise:
    case 1:
        print(text.upper())
    case 2:
        print(text.lower())
    case 3:
        print(text.title())
    case 4:
        print(text.capitalize())
