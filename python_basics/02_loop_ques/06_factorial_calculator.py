# Problem: Factorial Calculator
# Compute the factorial of a number using while loop

number_in = int(input("Enter the number you want the factorial of:\t"))
number = number_in
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
print(f"Factorial of {number_in} is: {factorial}")