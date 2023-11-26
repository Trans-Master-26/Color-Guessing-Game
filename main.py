print("Guess a color.")
color = input()
while True:
    print("Guess another color.")
    color = input()
    if color == "red":
        print("That is the color we were looking for!")
        break
    else:
        print("That is the wrong color, try again.")
