

def f(n):
    if n % 2 == 1:
        return n
    return f(n // 2)

print(f(int(input())))
