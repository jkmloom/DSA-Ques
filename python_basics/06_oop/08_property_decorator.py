# Problem: Use a poperty decorator in the Car_Store class to make the model attributes read-only.

class Car_Store:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand # '__' pre-variable makes it private to its class
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
    
    @property #makes the method '.model()' access like property '.model'
    def model(self):
        return self.__model
    

class Electric_Car(Car_Store):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"



jkmloom = Car_Store("Toyota", "Supra MK-5")
# jkmloom.model = "GR Corolla"

print(jkmloom.model)