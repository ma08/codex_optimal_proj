
#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/2/18
from collections import defaultdict
n = int(input())
a = [int(x) for x in input().split()]
d = defaultdict(int)
for i in a:
    d[i] += 1
print(len(d))
print(*d.keys())
