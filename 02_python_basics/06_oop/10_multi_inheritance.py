# Problem: Create two classes Battry nd Engine, and let the Inherit_Car class inherit from both, demonstrating multi-inhritance.

class Car_Store:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car_Store.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def car_full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are cool..!"
    
    @property
    def model(self):
        return self.__model
    

class Electric_Car(Car_Store):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"


class Battery:
    def battery_info(slef):
        return "This car has a powerful battery.."


class Engine:
    def engine_info(self):
        return "This is a popwerful engine.."


class Inherit_Car(Battery, Engine, Car_Store):
    pass

jkmloom = Inherit_Car("Tesla", "Model S (2025)")
print(jkmloom.engine_info())
print(jkmloom.battery_info())