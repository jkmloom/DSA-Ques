# Problem: Reverse a string using loop

input_string = input("Enter a word:\t")
reversed_string = ""

for char in input_string[-1::-1]:
    reversed_string += char
print(reversed_string)