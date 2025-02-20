class Animal:
    def Sound(self):
        print("animals make sounds")

class Dog(Animal):
    def Sound(self):
        super().Sound()
        print("dogs bark")

obj = Dog()
obj.Sound()