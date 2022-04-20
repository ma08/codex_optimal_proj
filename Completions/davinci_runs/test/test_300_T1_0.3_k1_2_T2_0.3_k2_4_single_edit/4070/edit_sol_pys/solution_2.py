
def f(n):
    if n == 0:
        return 0
    else:
        return n % 2 + f(n // 2)


print(f(int(input()))) 
