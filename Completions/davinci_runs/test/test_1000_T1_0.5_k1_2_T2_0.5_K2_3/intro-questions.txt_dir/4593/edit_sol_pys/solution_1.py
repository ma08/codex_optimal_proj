

def fun(x):
    if x == 0:
        return 1
    else:
        return x * fun(x - 1)

print(fun(5))
