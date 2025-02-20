this_dict = {
    "brand": "tata",
    "model": "nexon",
    "year": "2023",
    "year": "2024",
    "automatic": False

}
print(type(this_dict))

print(this_dict["brand"])
x = this_dict["model"]   #or x = this_dict.get("model")
print(x)
x = this_dict.values()
print(x)
x = this_dict.items()
print(x)

if "model" in this_dict:
    print("model exists")
else:
    print("not there")

this_dict.update({"model": "bmw"})
print(this_dict)

this_dict.update({"num": "pb"})
print(this_dict)

this_dict["color"] = "white"
print(this_dict)

this_dict.pop("automatic")
print(this_dict)

for x in this_dict:
    print(x)

for x in this_dict.values():
    print(x)
for x, y in this_dict.items():
    print(x, y)

my_dict = this_dict.copy()
print(my_dict)

# - Implement get_unique_customers(orders), which returns a set of unique customer names.
set = []
for x in this_dict:
    if x not in set:
        set.append(x)
print(set)
