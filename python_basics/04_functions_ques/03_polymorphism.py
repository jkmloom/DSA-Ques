# Problem: write a function 'multiply' that multiplies two numbers, but can also accept and multiply strings.

def multiply(fact_1, fact_2):
    return fact_1 * fact_2

print(multiply(8, 5))
print(multiply(8, '5'))
print(multiply('a', 5))
print(multiply(5, 'a'))