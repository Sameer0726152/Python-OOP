class Phone:
    total_phones = 0

    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        Phone.total_phones += 1

    @classmethod
    def get_total(cls):
        print(f"Total objects are {Phone.total_phones}")

    @classmethod
    def from_string(cls, data_string):
        brand, model, battery = data_string.split(", ")
        return cls(brand, model, int(battery))
        
    
    @staticmethod
    def is_valid_battery(level):
        return 0 <= level <= 100

    def charge(self, amount):
        self.battery = self.battery + amount
        if self.battery > 100:
            self.battery = 100
        print(f"Battery is {self.battery}%")

    def show_info(self):
        print(f"Brand is {self.brand}, Model is {self.model}, Battery is {self.battery}%.")

p1 = Phone("Iphone", 16, 60)
p2 = Phone("Samsung", "F17", 70)
p1.show_info()
p1.charge(30)
p2.show_info()
p2.charge(50)

p3 = Phone.from_string("Oppo, 18, 90")
p3.show_info()
Phone.get_total()
valid = Phone.is_valid_battery(100)
print(valid)