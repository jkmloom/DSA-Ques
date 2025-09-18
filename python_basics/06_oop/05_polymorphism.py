# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and Electric_Car classes, but with different behaviours.

class Car_Store:
    def __init__(self, brand, model):
        self.__brand = brand # '__' pre-variable makes it private to its class
        self.model = model

    def get_brand(self): # convention: start getter functions name with 'get_'
        return self.__brand + "!"

    def car_full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

# pass the class name as attribute to inherit that class
class Electric_Car(Car_Store):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"



tesla = Electric_Car("Tesla", "Model S (2025)", "100 kWh")
print(tesla.fuel_type())

land_rover = Car_Store("Land Rover", "Defender")
print(land_rover.fuel_type())