# Problem: List Uniqueness Checker
# Check if all the elements in a list are unique. if a duplicate is found, exit loop and print the duplicate.
# list: ['apple', 'banana', 'orange', 'mango']

fruits = ['apple', 'banana', 'apple', 'orange', 'mango'] # given list
unique_item = set()

for item in fruits:
    if item in unique_item:
        print(f"Duplicate Item: {item}")
        break
    unique_item.add(item)