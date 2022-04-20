



def twos_complement(n):
    if n == 0:
        return 0

    if n > 0:
        res = []
        while n > 0:
            res.append(str(n % 2))
            n //= 2
        return "".join(res[::-1])

    # n < 0
    n = abs(n)

    res = []
    while n > 0:
        if n % 2 == 0:
            res.append("1")
            n = (n // 2) + 1
        else:
            res.append("0")
            n //= 2

    return "1" + "".join(res[::-1])

import sys

n = int(sys.stdin.readline())

print(twos_complement(n))
