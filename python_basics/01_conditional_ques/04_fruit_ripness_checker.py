# Problem: Determine if the fruit is ripe, overrip, or unripe based on its color. (eg. Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"

if fruit == "Banana":
    print("Colors: Green, Yellow, Brown")
    fruit_color = input("Enter banana's color:\t")

    if fruit_color == "Green": print(f"{fruit} is: Uniripe")
    elif fruit_color == "Yellow": print(f"{fruit} is: Ripe")
    elif fruit_color == "Brown": print(f"{fruit} is: Overripe")
    else: print("Choose a right banana color..!")

else: print("Fruit not in database..!")