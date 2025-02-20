my_list = [1, 3, 4, 2, 6, 56, 78, 52.4, 67.9]

newlist = [x for x in my_list if x % 2 != 0]
print(newlist)

newlist = [x for x in my_list if type(x) == float]
print(newlist)

# newlist = [x for x in range(1, 1000) if x % 7 == 0]
# print(newlist)

# newlist = [x for x in range(1, 1000) if '3' in str(x)]
# print(newlist)
newlist = []
for x in my_list:
    newlist.append(x+1)
print(newlist)

newlist = [x+2 for x in my_list ]
print(newlist)

extra_list = ["mango", "kiwi", "banana"]
newlist = []
for x in extra_list:
    newlist.append(x.upper())
print(newlist)

for x in extra_list:
    newlist.append(x.lower())
print(newlist)

for x, y in enumerate(my_list):
    print(x, y)

newlist = []
for x in my_list:
    newlist.append(x * x)
print(newlist)

newlist = [x * x for x in my_list]
print(newlist)

newlist = [x for x in my_list if x % 2 == 0]
print(newlist)

newlist = [x[0] for x in extra_list]
print(newlist)

newlist = [x[::-1] for x in extra_list ]
print(newlist)

newlist = ["EVEN" if x % 2 == 0 else "ODD" for x in my_list]
print(newlist)