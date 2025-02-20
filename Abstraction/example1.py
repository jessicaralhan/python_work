from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def print_details(self):
        pass

    def accelerate(self):
        print("acceleration starts")

    def break_applied(self):
        print("stop")


class Hatchback(Car):
    def print_details(self):
        print("brand-", self.brand)
        print("year-" , self.year)

class SUV(Car):
    def print_details(self):
        print("brand-", self.brand)
        print("year-", self.year)

car1 = Hatchback("tata", "2023")
car1.print_details()
car1.accelerate()
car1.break_applied()

car2 = SUV("audi", "2024")
car2.print_details()