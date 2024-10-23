class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description (self):
        return f"{self.year} {self.make} {self.model}"  
    
my_car = Car("Toyota", "Camry", 2001)  
print(type(my_car))
print(dir(my_car))


