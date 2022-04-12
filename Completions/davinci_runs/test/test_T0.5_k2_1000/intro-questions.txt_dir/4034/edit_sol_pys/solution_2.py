

from collections import defaultdict
from typing import List, Dict, Tuple, Set
from sys import stdin, stdout
from itertools import chain

n = int(stdin.readline())
s = stdin.readline()

assert 1 <= n <= 200
assert len(s) == n
assert all(c.islower() for c in s)

def get_graph(s):
    graph = defaultdict(list)
    for i, c in enumerate(s):
        graph[c].append(i)
    return graph

def get_maximum_clique(graph):
    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    def bron_kerbosch(r, p, x): # r, p, x are sets of vertices
        nonlocal maximum_clique
        if len(p) == 0 and len(x) == 0:
            maximum_clique = max(maximum_clique, r, key=lambda clique: len(clique))
            return
        for v in list(p):
            bron_kerbosch(r | {v}, p & graph[v], x & graph[v])
            p.remove(v)
            x.add(v)

    maximum_clique = set()
    bron_kerbosch(set(), set(graph.keys()), set())
    return maximum_clique

def get_maximum_clique_size(graph):
    return len(get_maximum_clique(graph))

def get_maximum_clique_indices(graph):
    maximum_clique = get_maximum_clique(graph)
    return set(chain.from_iterable(graph[c] for c in maximum_clique))

def get_colors(s):
    colors = []
    for i, c in enumerate(s):
        colors.append('0' if i in get_maximum_clique_indices(get_graph(s)) else '1')
    return colors

def is_sorted(s):
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def is_sorted_after_swap(s):
    return is_sorted(s) or is_sorted(s[::-1])

colors = get_colors(s)

if is_sorted_after_swap(s):
    print("YES")
    print(''.join(colors))
else:
    print("NO")
