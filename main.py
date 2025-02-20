list = [12, 45, 6, 89]
# newlist = [x for x in list if x < 60] #list comprehension
# print(newlist)
print(list[1:3])   #list slicing

for i in list:       #using loop
    print(i)


list[1] = 46
print(list)

list[2:3] = [11]
print(list)

newlist = [x for x in list if x % 2 == 0]
print(newlist)

a = 8
b = 10
print(max(a,b))
print(min(a,b))


if a > b:
    print(a)
else: 
    print(b)

print(len(list))
list.append(70)
print(list)

list[0], list[4] = list[4], list[0]
print(list)

temp = list[1]
list[1] = list[4]
list[4] = temp

print(list)
list.reverse()
print(list)

print(max(list))
print(min(list))

rev = list[::-1]
print(list)


list.append(89)

seen = set()
dup = []
for x in list:
    if x in seen:
        dup.append(x)
    else:
        seen.add(x)

print (dup)


list = [1, 2, 3, 4, 5, 4, 3, 2]

print(list)

print(max(list))
print(min(list))

rev = list[::-1]

seen = set()
dup = []

for x in list:
    if x in seen:
        dup.append(x)
    else:
        seen.add(x)

print(dup)

list[1], list[4] = list[4], list[1]
print(list)

double = []

for x in list:
    double.append(x+2)
print(double)

for x, v in enumerate(list):
    print(f"index {x}: {v}")


set = []

for x in list:
    if x not in set:
        set.append(x)

print(set)