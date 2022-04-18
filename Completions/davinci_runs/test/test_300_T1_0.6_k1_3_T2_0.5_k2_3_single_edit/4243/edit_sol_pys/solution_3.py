
from collections import defaultdict

def happiness(x):
    n = [500, 100, 50, 10, 5, 1]
    d = defaultdict(int)
    for i in range(len(n)):
        d[n[i]] = x // n[i]
        x %= n[i]
    return 1000 * d[500] + 5 * d[5]

if __name__ == '__main__':
    x = int(input())
    print(happiness(x))
