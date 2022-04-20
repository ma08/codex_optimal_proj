

#-----Solution-----

n, m = map(int, input().split())

def func(n, m):
    if n == m:
        return 0
    elif n > m:
        return -1
    elif m % 2 == 0:
        return 1 + func(n, m // 2)
    else:
        return 1 + func(n, m * 2)

print(func(n, m))