
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    c = Counter(s)
    print(min(c['a'], c['b']))
