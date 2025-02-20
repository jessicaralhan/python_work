class Animal:
    def sound(self):
        print("animals sounds")

class Tiger(Animal):
    def sound(self):
        super().sound()
        print("tiger roars")

class Dog(Animal):
    def sound(self):
        print("woofs")

def play_sound(Animal):
    Animal.sound()

tiger = Tiger()
dog = Dog()

play_sound(tiger)
play_sound(dog)
