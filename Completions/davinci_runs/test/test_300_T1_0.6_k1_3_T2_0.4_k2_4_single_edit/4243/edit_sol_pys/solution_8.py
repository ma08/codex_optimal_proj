

from collections import defaultdict

def happiness(n):
    n = [500, 100, 50, 10, 5, 1]
    d = defaultdict(int)
    for i in range(len(n)):
        d[n[i]] = n // n[i]
        n %= n[i]
    return 1000 * d[500] + 5 * d[5]

n = int(input())
print(happiness(n))
