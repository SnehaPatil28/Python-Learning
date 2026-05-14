print("Color Mixer")

colors = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
}

while True:
    color1 = input("Enter the first color:").lower()
    color2 = input("Enter the second color:").lower()

    mix = None
    if (color1, color2) in colors:
        mix = colors[(color1, color2)]

    if mix:
        print(f"When you mic {color1} and {color2}, you get {mix}!")
    else:
        print("I don't know what those colors make when mixed")

    if not input("Mix more colors?").lower().startswith("y"):
        print("Goodbye!!")
        break
