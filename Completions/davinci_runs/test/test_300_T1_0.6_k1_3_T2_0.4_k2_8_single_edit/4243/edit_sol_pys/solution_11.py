from collections import defaultdict

def happiness(x):
    n = [500, 5]
    d = defaultdict(int)
    for i in range(len(n)):
        d[n[i]] = x // n[i]
        x %= n[i]
    return 1000 * d[500] + 5 * d[5]

x = int(input())
print(happiness(x))
