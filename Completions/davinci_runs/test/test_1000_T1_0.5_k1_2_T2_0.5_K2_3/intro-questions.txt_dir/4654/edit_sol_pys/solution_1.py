
def f(n):
    if n == 0:
        return 0
    elif n < 10:
        return n
    else:
        return f(n // 10) + n % 10


n = int(input())
print(f(n))
