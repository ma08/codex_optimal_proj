

def coconut_splat(s, n, k):
    if n == 1:
        return 1
    elif s == 9:
        if (n - 1) % 2 == 0:
            return 1
        else:
            return 2
    else:
        if (n - 1) % 3 == 0:
            return 1
        elif (n - 1) % 3 == 1:
            return 2
        else:
            return 3

s, n, k = map(int, input().split())
print(coconut_splat(s, n, k))
