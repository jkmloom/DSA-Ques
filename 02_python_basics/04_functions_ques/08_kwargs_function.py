# Problem: Create a function that accepts any number of keyword arguments and print them in the format key:value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Shaktiman")
print_kwargs(power = "Lazer", name = "Shaktiman")
print_kwargs(power = "Lazer", name = "Shaktiman", enemy = "Dr. Jackaal")