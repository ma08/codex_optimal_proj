#!/usr/bin/env python3

from collections import Counter
from itertools import accumulate

n, *a = map(int, open(0).read().split())
c = Counter(accumulate(a))

print(*[c[i] for i in range(n)])
