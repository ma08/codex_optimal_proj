
from collections import defaultdict

def happiness(x):
    n = [500, 5, 100, 50, 10, 1]
    d = defaultdict(int)
    for i in range(len(n)):
        d[n[i]] = x // n[i]
        x %= n[i]
    return 1000 * d[500] + 5 * d[5] + 100 * d[100] + 50 * d[50] + 10 * d[10] + d[1]

x = int(input())
print(happiness(x))
