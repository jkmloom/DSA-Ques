# Problem: add a static method to the Car_Store that returns a general description of a car

class Car_Store:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand # '__' pre-variable makes it private to its class
        self.model = model
        Car_Store.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def car_full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # static methods can't be called through instances/objects
    @staticmethod # makes the method static
    def general_description():
        return "Cars are cool..!"
    

class Electric_Car(Car_Store):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"



jkmloom = Car_Store("Toyota", "Supra MK-5")
print(jkmloom.general_description())
print(Car_Store.general_description())

print(Car_Store.total_car)