for x in range(1,11):
    print(x)

for x in range(1,50):
    if x % 2 == 0:
        print("even numbers", x)
    # else:
    #     print("odd numbers")

for x in "mango":
    print(x)

fruits = ["mango", "banana", "apple"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

n = int(input())
sum = 0

for n in range (1,n+1):
    sum += n
    print("sum is", sum)

factorial = 1
for n in range(1,n + 1):
    factorial *= n
    print(f" factotial of {n} is {factorial}")
    print(factorial)