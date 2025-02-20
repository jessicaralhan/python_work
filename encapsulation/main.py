class Dog:
    def __init__(self, name, breed, age):
        self.name = name 
        self._breed = breed
        self.__age = age
    
    def get_info(self):
         return f"name : {self.name}, breed : {self._breed}, age : {self.__age}"
   
    def get_age(self):
            return self.__age
        
    def set_age(self, age):
            if age > 0:
                self.__age = age
            else:
                print("age must be positive")

dog = Dog("lemon", "Beagle", 2)
print(dog.name)
print(dog._breed)
print(dog.get_age())
dog.set_age(-1)
print(dog.get_info())