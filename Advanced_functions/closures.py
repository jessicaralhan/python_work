def func1(x):
    def func2(y):
        return x + y
    return func2 
closure = func1(10)
print(closure(5))