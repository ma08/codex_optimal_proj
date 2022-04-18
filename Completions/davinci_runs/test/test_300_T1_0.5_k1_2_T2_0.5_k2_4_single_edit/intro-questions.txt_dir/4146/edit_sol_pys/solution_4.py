import numpy as np
import math
import itertools
import sys
import heapq
import bisect
import copy
import collections
import fractions
import random
import string
import time

import sys

n = int(input())
v = list(map(int, input().split()))

a = [0] * (10**5 + 1)
for i in v:
    a[i] += 1

a.sort()

ans = 0
if a[-1] == a[-2]:
    ans = 0
else:
    ans = a[-1] - a[-2]

print(ans)
