# Problem: Add a class variable to Car_Store that keeps track of the number of crs created

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

tata = Car_Store("Tata", "Nexon")
print(tata.fuel_type())

print(Car_Store.total_car)