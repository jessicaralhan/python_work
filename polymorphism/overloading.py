class Mathoperations:          #using default arguments 
    def add(self, a, b, c=0):
        return a + b + c
    
mathop = Mathoperations()
print(mathop.add(7,7,2))
print(mathop.add(2,2,3))

class Mathoperations:          #using *args
    def add(self, *args):
        return sum(args)
    
mathop = Mathoperations()
print(mathop.add(7,7,2))
print(mathop.add(1,1,1))