class Animal:
    def Sound(self):
        print("animals makes sounds")

class Dog(Animal):
    def barks(self):
        print("dog barks")

obj = Dog()
obj.Sound()
obj.barks()