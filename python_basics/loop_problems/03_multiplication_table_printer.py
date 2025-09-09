# Problem: Multiplication Table Printer
# Print the multiplication table for a given number upto 10, but skip the fith iteration.

number = int(input("Enter a number:\t"))

for num in range(1, 11):
    if num == 5: continue
    print(f"{number} * {num} = {number * num}")