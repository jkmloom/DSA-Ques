# Problem: Sum of even numbers
# Calculate the sum of even numbers up to a given number 'n'.

number = int(input("Enter a number to calculate the sum:\t"))
number_sum = 0

for num in range(0, number + 1, 2):
    number_sum += num
print(f"Sum of even numbers upto {number} is: {number_sum}")