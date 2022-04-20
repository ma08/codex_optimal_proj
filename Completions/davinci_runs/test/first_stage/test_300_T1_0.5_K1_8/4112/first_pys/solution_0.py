

import random

def max_beauty(n, k, x, a):
    if k == 1:
        return sum(a)

    if k == 2:
        return sum(a)

    if x == 1:
        return max(a)

    if k == x:
        return sum(a)

    if k == n:
        return sum(a)

    if x == n:
        return sum(a)

    # k < x
    if k < x:
        if k == 2:
            return sum(a) - min(a)
        else:
            return sum(a) - min(a) - min(a[1:-1])

    # k > x
    if k > x:
        if x == 2:
            return sum(a) - min(a)
        else:
            return sum(a) - min(a) - min(a[1:-1])

    return -1


if __name__ == "__main__":
    n = random.randint(1, 5000)
    k = random.randint(1, n)
    x = random.randint(1, n)
    a = [random.randint(1, 10**9) for i in range(n)]

    print(n, k, x, a)
    print(max_beauty(n, k, x, a))