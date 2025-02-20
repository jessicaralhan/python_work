class Parent:
    def func1(self):
        print("this is parent class")

class Child(Parent):
    def func2(self):
        print("this is child class")

object = Child()
object.func1()
object.func2()
