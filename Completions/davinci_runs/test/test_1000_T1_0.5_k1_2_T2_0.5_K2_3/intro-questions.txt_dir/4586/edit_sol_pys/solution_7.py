def c(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


print(c(int(input()), 2))
