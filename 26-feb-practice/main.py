name_list = ["ajay", "yachika"]
# declare a variable and assign the vowels to it a, e, i, o, u
vowels = ['a', 'e', 'i', 'o', 'u']
for name in name_list:
 
    variable_count = 0
    index_count = 0
    
    for char in name:  
        index_count += 1

        if char in vowels:
            # break# index = name.index(char) 
            
            variable_count += 1
            
        print(f"index of {char} is {index_count}")                
        # index_count += 1
    print(f"{name} has {variable_count} vowels in total  ")
    
print(name_list)

# output should be in the format where it returns a list of dictionary inside a dictionary



output = [[0,{"ajay":{"vowel_count":2,"consonant_count":2}}],[1,{"yachika":{"vowel_count":3,"consonant_count":4}}]]
print(output[1][1]["yachika"]["vowel_count"])



















# # declare a variable and assign the vowels to it a, e, i, o, u
# vowels = ['a', 'e', 'i', 'o', 'u']
# print(type(vowels))
# # iterate over the string and check for these vowels and count it
# #n = jessica
# for name in name_list: # 1st = x = j 2nd = x = e 3rd = x = s 4th = x = s 5th = x = i 6th = x = c 7th = x = a
#     if name in vowels : 
#         # 1st = j in ['a', 'e', 'i', 'o', 'u'] 
#        # 2nd = e in ['a', 'e', 'i', 'o', 'u'] 
#        # 3rd = s in ['a', 'e', 'i', 'o', 'u']
#        # 4th = s in ['a', 'e', 'i', 'o', 'u'] 
#        # 5th = i in ['a', 'e', 'i', 'o', 'u']
#        # 6th = c in ['a', 'e', 'i', 'o', 'u']
#        # 7th = a in ['a', 'e', 'i', 'o', 'u']
        
#         print(char)          # 2nd = e 5th = i  7th = a
# # count the number of x how many vowels there are in x 


# name_list = ["jeessica", "yachika"]
# # declare a variable and assign the vowels to it a, e, i, o, u
# vowels = ['a', 'e', 'i', 'o', 'u']
# for name in name_list:
#     # print(name)
    
# # x = char.index("a")
# # print(x)


#     variable_count = 0
    
#     for index, char in enumerate(name):  
#         if char in vowels:
#             # index = name.index(char) 
            
#             variable_count += 1
        
#             print(f"index of {char} is {index}")
#     print(f"{name} has {variable_count} vowels in total  ")