my_tuple = (1, 2, 3, 4, 5, 5, 4)
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))
items = tuple(("jessica",))
print(items)
print(my_tuple[2])
print(my_tuple[-2])
print(my_tuple[2:5])
print(my_tuple[:3])
print(my_tuple[5:])

key = 2
flag = False

for x in my_tuple:
    if x == key:
        flag = True
        
if flag:
        print("element is foubd")
else:
        print("not found")

y = list(my_tuple)    #change values in a tuple 
y[1] = 44
my_tuple = tuple(y)
print(my_tuple)

z = list(my_tuple)
z.append("jessica")
my_tuple = tuple(z)
print(my_tuple)

fruits = ("apple", "banana", "cherry", "apple", "banana", "mango")
(x, *y, z) = fruits
print(x, y, z)

for x in range(len(fruits)):
      print (fruits[x])

for x in range(len(my_tuple)):
      print(my_tuple[x])

x = 0
while x < len(fruits):
      print(fruits[x])
      x = x + 1

# i = 1
# while i < len(fruits):
#       print(fruits[i])
#       i = i+1

tuple1 = ("jess", "yach", "jess", "yach")
tuple2 = ("vish", "lem", "vish", "lem")

tuple3 = tuple1 + tuple2
print(tuple3)

names = tuple3 * 2
print(names)

print(names[6:])
names1 = names.count("vish")
names2 = tuple2.index("lem")
print(names1)
print(names2)