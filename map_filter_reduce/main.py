from functools import reduce
my_list = [1, 2, 3, 4, 5]

double = list(map(lambda x: x * 2, my_list))
print(double)

double = [x * 2 for x in my_list]
print (double)

even = list(filter(lambda x : x % 2 == 0, my_list))
print(even)

odd = list(filter(lambda x : x % 2 != 0, my_list))
print(odd)

value = reduce(lambda x, y: x + y, my_list)
print(value)