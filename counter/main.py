from collections import Counter, defaultdict

list = ["man", "go", "starw", "berry", "rasp", "berry", "rasp"]
list_count = Counter(list)
print(list_count)

list_count = Counter(list)
print(list_count.most_common(2))


num_list = defaultdict(int)
num_list["strawberry"] = 20

print(num_list["strawberry"])
print(num_list["mango"])



list_count = Counter(list)
print(list_count)

num_list = defaultdict(int)
num_list["mango"] = 30

print(num_list["strawberry"])
print(num_list["mango"])