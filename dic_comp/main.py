list = [1, 3, 4, 5, 8]
newlist = {x : x ** 3 for x in list if x % 2 != 0}
print(newlist)

newlist = {x : x+2 for x in list}
print(newlist)

numbers = range(10)
newlist = {x : x**2 for x in list if x % 2 == 0}
print(newlist)

original = {"a" : 1, "b" : 5}
swapped = {value : key for key, value in original.items()}
print(swapped)