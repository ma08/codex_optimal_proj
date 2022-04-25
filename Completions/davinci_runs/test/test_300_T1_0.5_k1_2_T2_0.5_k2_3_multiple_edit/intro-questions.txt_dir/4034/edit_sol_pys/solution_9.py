

from collections import defaultdict
from typing import List, Dict, Tuple, Set
from sys import stdin, stdout
from itertools import chain

n = int(stdin.readline())
s = stdin.readline()

assert 1 <= n <= 200
assert len(s) == n
assert all(c.islower() for c in s)
