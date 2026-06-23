class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"Brand is {self.brand}, It gives speed of {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def describe(self):
        super().describe()
        print(f"Number of doors are {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_sidecar):
        super().__init__(brand, speed)
        self.has_sidecar = has_sidecar
    
    def describe(self):
        super().describe()
        print(f"Has a sidecar? {self.has_sidecar}")

c1 = Car("Toyota", "180km/hr", 4)
b1 = Bike("Yamaha", "220km/hr", False)
c1.describe()
b1.describe()
print(isinstance(c1, Vehicle))
print(isinstance(b1, Vehicle))