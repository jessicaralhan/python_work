squares = {x ** 2 for x in range(1, 20)}
print(squares)


states = ['punjabi', 'chandigarh', 'goa']
states2 = ['jaipur', 'rajashtahn', 'manipur']

total = {key:value for (key, value) in zip(states, states2)}
print(total)

text = "jessica"
newset = {x for x in text}
print(newset)

#it is used to combine multiple interable together or it takes first element in each interable and pair it together and then takes second element and pair it together
name = ["jessica", "yachika", "lemon"]
age = [21, 28]
color = ["pink", "blue", "beige"]

newlist = zip(name, age, color)
print(list(newlist))

for name, age in zip(name, age):
    print(f"name: {name}, age: {age}")



zipped_list = [('jessica', 21), ('yachika', 28)]
name, age = zip(*zipped_list)
print(name)
print(age)


list = [('chandigarh','far'), ('kharar', 'near')]
place, distance = zip(*list)
print(place)
print(distance)