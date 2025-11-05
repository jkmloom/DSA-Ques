# Problem: Create an ElectricCar class that has an additional attribute batter_size

class Car_Store:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_full_name(self):
        return f"{self.brand} {self.model}"
    

# pass the class name as attribute to inherit that class
class Electric_Car(Car_Store):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    

car_jkmloom = Electric_Car("Tesla", "Model S (2025)", "100 kWh")
print(car_jkmloom.car_full_name())

car_jkmjatin = Electric_Car("BYD", "eMAX 7", "71 kWh")
print(car_jkmjatin.car_full_name())