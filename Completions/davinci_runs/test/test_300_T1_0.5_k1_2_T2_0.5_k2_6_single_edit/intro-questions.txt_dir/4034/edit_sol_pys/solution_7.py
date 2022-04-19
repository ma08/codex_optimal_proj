

from collections import defaultdict
from typing import List, Dict, Tuple, Set
from sys import stdin, stdout
from itertools import chain

n = int(stdin.readline())
s = stdin.readline()

assert 1 <= n <= 2 * 10**5
assert len(s) == n
assert all(c in '01' for c in s)

def get_max_clique_size(s):
    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    def bron_kerbosch(r, p, x):
        nonlocal max_clique_size
        if len(p) == 0 and len(x) == 0:
            max_clique_size = max(max_clique_size, len(r))
            return
        for v in list(p):
            bron_kerbosch(r | {v}, p & graph[v], x & graph[v])
            p.remove(v)
            x.add(v)

    graph = defaultdict(set)
    for i, c in enumerate(s):
        graph[c].add(i)

    max_clique_size = 0
    bron_kerbosch(set(), set(graph.keys()), set())
    return max_clique_size

def is_sorted(s):
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def is_sorted_after_swap(s):
    return is_sorted(s) or is_sorted(s[::-1])

max_clique_size = get_max_clique_size(s)

if max_clique_size <= 1 or is_sorted_after_swap(s):
    print("YES")
    print(''.join('0' if i < max_clique_size else '1' for i in range(n)))
else:
    print("NO")
