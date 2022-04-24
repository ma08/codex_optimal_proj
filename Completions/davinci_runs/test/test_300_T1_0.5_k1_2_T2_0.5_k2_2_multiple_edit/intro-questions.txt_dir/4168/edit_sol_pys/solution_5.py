

def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 2)
    return f(n // 2) + 1

print(f(n))
