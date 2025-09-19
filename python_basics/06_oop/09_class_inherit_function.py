# Problem: Demonstrate the use of isinstance() to check if 'jkmloom' is an instance of Car_Store and Electic car

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



jkmloom = Electric_Car("Tesla", "Model S (2025)", "100 kWh")

print(isinstance(jkmloom, Car_Store))
print(isinstance(jkmloom, Electric_Car))
