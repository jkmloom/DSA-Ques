# Problem: Recommend a type of pet food based on the pet's spicies and age. (eg. Dog <2 years - puppy food, Cat: >5 years - senior cat food)

food_list = ['Puppy Food', 'Senior Cat Food']

animal = input("Which animal do you have (dog/cat):\t")
animal = animal[0].upper() + animal[1:].lower()

if animal == 'Cat':
    animal_age = int(input("🐈 Enter cat's age (in years):\t"))
    if animal_age > 5: print(f"Recommended Food: {food_list[1]}")
    else: print("No recommendation availabl..!")

elif animal == 'Dog':
    animal_age = int(input("🐕 Enter dog's age (in years):\t"))
    if animal_age < 2: print(f"Recommended Food: {food_list[0]}")
    else: print("No recommendation availabl..!")

else: print("🥲 No data available for this animal..!")