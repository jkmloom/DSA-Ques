# Problem: Basic Class and Objcet
# Create a Car class with attributes like brand and model. Then create an instance of this class.

'''
"Constructor" is a method. Whenever an object is created using a class, the constuctor (method) is called before anything else.
'''

class Car_Class:
    # __init__ is the constructor in Python
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Car owned by user: @jkmloom
car_jkmloom = Car_Class("Toyota", "Supra MK-5")
print(car_jkmloom.brand)
print(car_jkmloom.model)

# Car owned by user: @jkmjatin
car_jkmjatin = Car_Class("Mazda", "RX-8")
print(car_jkmjatin.brand)
print(car_jkmjatin.model)