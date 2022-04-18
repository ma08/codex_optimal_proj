def f(x):
    if x == 1:
        return 1
    else:
        return f(x-1) * x


print(f(5))
