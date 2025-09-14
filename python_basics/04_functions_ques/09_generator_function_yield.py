# Probllem: write a generator functoin that yeilds even numbers up to a specified limit.

def yield_generator(limit):
    for i in range(0, limit + 1, 2):
        yield i

for num in yield_generator(10):
    print(num, end=" ")