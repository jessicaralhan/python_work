class Car:
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year

    def  display_info(self):
        print(f"car: {self.brand}, model: {self.model}, year: {self.year}")

carobj = Car("tata", "nexon", "2024")
carobj.display_info()


class Smartphone:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def description(self):
        print(f"mobile is of {self.model} model and made in year {self.year} ")

Smartphoneobj = Smartphone("iphone", "2023")
Smartphoneobj.description()
        