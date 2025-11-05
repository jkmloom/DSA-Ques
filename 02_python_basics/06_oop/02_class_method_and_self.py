# Problem: add mehtod to the 'Car_Store' class that displays the full name of the cars (brand and model).

class Car_Store:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_full_name(self):
        return f"{self.brand} {self.model}"
    

car_jkmloom = Car_Store("McLAREN", "750S Spider")
print(car_jkmloom.car_full_name())

car_jkmjatin = Car_Store("Porsche", "Taycan Turbo S")
print(car_jkmjatin.car_full_name())