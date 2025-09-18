# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and providing a getter method for it.

class Car_Store:
    def __init__(self, brand, model):
        self.__brand = brand # '__' pre-variable makes it private to its class
        self.model = model

    def get_brand(self): # convention: start getter functions name with 'get_'
        return self.__brand + "!"

    def car_full_name(self):
        return f"{self.__brand} {self.model}"
    

# pass the class name as attribute to inherit that class
class Electric_Car(Car_Store):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



car_jkmloom = Electric_Car("Tesla", "Model S (2025)", "100 kWh")
print(car_jkmloom.get_brand())
