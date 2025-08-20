class Laptops():
    def __init__(self, make, model, color, year, serialNumber):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.serialNumber = serialNumber

    def __str__(self):
        return f"{self.make}, {self.model}, {self.color}, {self.year}, {self.serialNumber}"
    
laptop1 = Laptops("Dell", "Alienware", "Black", 2003, "SN-111")
laptop2 = Laptops("Dell", "XPS", "Green", 1993, "SN-141")
laptop3 = Laptops("HP", "Victus", "White", 2023, "SN-251")
laptop4 = Laptops("HP", "Omen", "Silver", 2015, "SN-673")
laptop5 = Laptops("Dell", "Inspiron", "Black", 2025, "SN-931")


print(laptop1)
print(laptop2)
print(laptop3)
print(laptop4)
print(laptop5)