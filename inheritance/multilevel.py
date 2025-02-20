class Animal:
    def sound(self):
        print("Animals makes sound")
        
class Dog(Animal):  
    def bark(self):
        print("dog barks")

class Cat(Dog):
    def meow(self):
        print("cat meows")

A = Cat()
A.sound()
A.bark()
A.meow()