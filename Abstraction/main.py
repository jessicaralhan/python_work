from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "car engine strat"
    
    def stop_engine(self):
        return "engine stop"
        

class Food(ABC):
    @abstractmethod
    def making_food(self):
        pass
    @abstractmethod 
    def cook_food(self):
        pass

class Pizza(Food):
    def making_food(self):
        return "made food"
    
    def cook_food(self):
        return "cookded food "