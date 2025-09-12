# Problem: Create a function that returns both the area and circumference of a circle given it's radius.

import math

def circle_math(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circle_math(3)
print(f"Area: {round(area, 2)} sq. units, Circumference: {round(circumference, 2)} units")