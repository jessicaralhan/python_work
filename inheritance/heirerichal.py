class Animal:
    def sounds(self):
        print("animals makes sounds")

class Dog(Animal):
    def barks(self):
        print("dog barks")

class Cat(Animal):
    def meows(self):
        print("cat meows")

dog = Dog()
cat = Cat()
dog.sounds()
dog.barks()
cat.sounds()
cat.meows()