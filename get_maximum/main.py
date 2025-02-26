# my_list = [12, 23, 100, 56, 8]

# print(max(my_list))

# # print(my_dict)
# temp = 0
# for x in my_list:
#     if x > temp:  #x = 12, 12 > 0, temp = 12,  x = 23, 23 > 12, temp 23,   x = 100, 100 > 23, temp 100,    x = 56, 56>100, temp 100,   x = 8, 8> 100, temp 100
#         temp = x #temp = 12, 23, 100
# print(temp)


my_dict = {
    "age" : 20,
    "age1" : 21,
    "age2" : 34,
    "age3" : 18,
    "age4" : 4
}
temp = 0
key_value = ""
for key, value in my_dict.items():
    print(key, value)
    if value > temp:
        temp = value
        key_value = key
print(key_value, temp)

print(my_dict)
