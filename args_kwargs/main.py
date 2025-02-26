def greet(*args):
    for name in args:
        print(f"hello: {name}")
greet("jessica", "yachika")


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

info(name = "jessica", age = 21)

my_list = [1, 2, 3, 4, 5]
newlist = [x * 2 for x in my_list]
print (newlist)