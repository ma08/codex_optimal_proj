# -*- coding: utf-8 -*-
import math
import bisect
from collections import Counter
from collections import defaultdict
from collections import deque
import heapq as hq
from itertools import product
from itertools import combinations
import sys
import bisect
import random
from decimal import Decimal
from operator import itemgetter
from fractions import gcd


n, t = map(int, input().split())

c = []
for i in range(n):
	c.append(list(map(int, input().split())))

c.sort(key=lambda x:x[0])
for i in c:
	if i[1] <= t:
		print(i[0])
		exit()
print("TLE")
