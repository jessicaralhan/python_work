my_set = {1, 2, 3, 4, "j", "y"}
for x in my_set:
    print(x)

print(2 in my_set)
print( 2 not in my_set)

my_set.add(56)
print(my_set)

anything = {"y", "j", 1}

# my_set.update(anything)
# print(my_set)

# my_set.remove("y")
# print(my_set)

# another = my_set.union(anything)
# print(another)

another = my_set.intersection(anything)
print(another)


another = my_set.difference(anything)
print(another)

my_set.symmetric_difference_update(anything)
print(my_set)