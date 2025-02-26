# x = int(input())
# print(x)
# if x % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# if x > 0:
#     print("positive number")
# elif x == 0:
#     print("zero")
# else: 
#     print("negative number")

# y = 23
# z = 100
# if y > z:
#     print("y is greater")
# else:
#     print("z is greater")

# if x % 5 == 0 and x % 11 == 0:
#     print("divisivle by both ")
# elif x % 5 == 0:
#     print("only by 5")
# elif x % 11 == 0:
#     print("only by 11")


# if x % 400 == 0:
#     print("it is a leap year")
# elif x % 4 == 0 and x % 100 != 0:
#     print("also a leap year")
# else:
#     print("not a leap year")


# marks = int(input())
# if marks > 90:
#     print("grade A")
# elif marks > 80 and marks < 89:
#     print("grade B")
# elif marks > 70 and marks < 79:
#     print("grade C")
# elif marks > 60 and marks < 69:
#     print("grade D")
# elif marks < 60:
#     print("grade F")

# s1 = 50
# s2 = 50
# s3 = 49
# if s1 == s2 == s3:
#     print("it is a triangle")
# else:
#     print("not one")


# x = input().lower()
# if x in ["a", "e", "i", "o", "u"]:
#     print("it a vowel")
# else: 
#     print("it is a consonant")


# x = int(input("x is "))
# y = int(input("y is "))
# oper = input("operator is ")

# if oper == "+":
#     print(x + y)
# elif oper == "-":
#     print(x - y)
# elif oper == "*":
#     print(x*y)
# elif oper == "/":
#     print(x/y)


# acc_balance = int(input("Enter acc balance"))
# withdrawl = int(input("winthdrawl amount"))
# if acc_balance >= withdrawl:
#     print("withdrawl done")
# else: 
#     print("balanace must be enough")


# purchased_amount = int(input("tell amount"))
# if purchased_amount > 5000:
#     discount = purchased_amount * 0.50
#     final_amount = purchased_amount - discount
#     print("10% discount applied", final_amount)
# else: 
#     discount = 0
#     final_amount = purchased_amount
#     print("no discount")

number = int(input("number between 1-7"))
days = {
    1 : "monday",
    2 : "tuesday",
    3 : "wednesday",
    4 : "thursday",
    5 : "friday",
    6 : "saturday",
    7 : "sunday"
}
if 1 <= number <= 7:
    print(f"day is {days[number]} ")
else:
    print("number again")