from collections import defaultdict

def happiness(x, n):
    d = defaultdict(int)
    for i in range(len(n)):
        d[n[i]] = x // n[i]
        x %= n[i]
    return d

x = int(input())
print(happiness(x))
