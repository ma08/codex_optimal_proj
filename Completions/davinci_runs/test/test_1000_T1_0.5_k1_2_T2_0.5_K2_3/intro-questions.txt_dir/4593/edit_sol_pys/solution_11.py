

def fun(x=0):
    if x == 0:
        return 1
    else:
        return x * fun(x - 1)

print(fun(x=5))
