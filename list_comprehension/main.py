from collections import Counter
# my_list = [1, 3, 4, 2, 6, 56, 78, 52.4, 67.9]

# newlist = [x for x in my_list if x % 2 != 0]
# print(newlist)

# newlist = [x for x in my_list if type(x) == float]
# print(newlist)

# # newlist = [x for x in range(1, 1000) if x % 7 == 0]
# # print(newlist)

# # newlist = [x for x in range(1, 1000) if '3' in str(x)]
# # print(newlist)
# newlist = []
# for x in my_list:
#     newlist.append(x+1)
# print(newlist)

# newlist = [x+2 for x in my_list ]
# print(newlist)

# extra_list = ["mango", "kiwi", "banana"]
# newlist = []
# for x in extra_list:
#     newlist.append(x.upper())
# print(newlist)

# for x in extra_list:
#     newlist.append(x.lower())
# print(newlist)

# for x, y in enumerate(my_list):
#     print(x, y)

# newlist = []
# for x in my_list:
#     newlist.append(x * x)
# print(newlist)

# newlist = [x * x for x in my_list]
# print(newlist)

# newlist = [x for x in my_list if x % 2 == 0]
# print(newlist)

# newlist = [x[0] for x in extra_list]
# print(newlist)

# newlist = [x[::-1] for x in extra_list ]
# print(newlist)

# newlist = ["EVEN" if x % 2 == 0 else "ODD" for x in my_list]
# print(newlist)

# newlist = sorted(my_list, reverse=True)
# print(newlist)


# my_list = [1, 2, 3, 4, 5]
# newlist = [x * 2 for x in my_list]
# print (newlist)

grades = [70, 46, 90, 34, 87]
newlist = [x for x in grades if x >= 40]
print(newlist)


square = {x : x ** 2 for x in range(0, 5)}
print(square)

unique = ["i", "am", "am", "done"]
newlist = list({x : x for x in unique})
print(newlist)


newlist = list(map(lambda x : x ** 2, grades))
print(newlist)

newlist = list(filter(lambda x : x % 2 == 0, grades))
print(newlist)

# newlist = reduce(lamda x, y : x + y, grades )


color = ["red", "green", "blue"]
for x , y in enumerate(color):
    print(x, y)

def greet(*args):
    for name in args:
        print(f"name : {name}")
greet("jessica")

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
info(name = "jessica", age = 21)

newlist = Counter(color)
print(newlist)

list = ['a', 'b', 'c']
x, y, z = list
print(x, y, z)

newlist = [x*2 for x in range(1000)]
print(newlist)
nums = 1, 3, 4
a, b, c = nums 