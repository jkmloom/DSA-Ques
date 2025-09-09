# Problem: Find the first non-repeated character
# Given a string, find the first non-repeated character

input_string  = input("Enter any word:\t") # hard coded

for char in input_string:
    if input_string.count(char) == 1: print(f"First Non Repeating Character: {char}")
    break