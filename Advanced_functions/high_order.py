#passing function as an argument

def sqaure(x):
    return x * x

def apply_function(func, value): 
    return func(value)

print(apply_function(sqaure, 5 ))

#returning function as a result 

def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(3)
print(double(2))

#map() to double the numbers 

def double(x):
    return x * 2
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(double, numbers))

print(doubled_numbers)

#map() to add the numbers 
def  add(x):
    return x + 2

numbers = [1, 2, 3, 4, 5]
add_numbers = list(map(add, numbers))
print(add_numbers)

#map to subtract the numbers

def sub(x):
    return x - 2

numbers = [4, 5, 6, 7]
subtract_numbers = list(map(sub, numbers))
print(subtract_numbers)

#filter() 

def is_even(x):
    return x % 2 == 0 

numbers = [6, 10, 21, 26, 55]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)