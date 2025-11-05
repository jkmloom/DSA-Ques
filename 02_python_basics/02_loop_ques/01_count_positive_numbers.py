# Problem: Counting Positive Numbers
# Given a list of numbers, count how many numbers are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10] # given
positive_number_count = 0

for val in numbers:
    if val > 0: positive_number_count += 1
print(f"Positive number count: {positive_number_count}")