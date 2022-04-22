

from collections import defaultdict
from typing import List, Dict, Set
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

def get_max_clique(graph: Dict[str, List[int]]) -> Set[str]:
    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    def bron_kerbosch(r: Set[str], p: Set[str], x: Set[str]):
        nonlocal max_clique
        if len(p) == 0 and len(x) == 0:
            max_clique = max(max_clique, r, key=len)
            return
        for v in list(p):
            bron_kerbosch(r | {v}, p & graph[v], x & graph[v])
            p.remove(v)
            x.add(v)

    max_clique = set()
    bron_kerbosch(set(), set(graph.keys()), set())
    return max_clique

def get_max_clique_size(graph: Dict[str, List[int]]) -> int:
    return len(get_max_clique(graph))

def get_max_clique_indices(graph: Dict[str, List[int]]) -> Set[int]:
    max_clique = get_max_clique(graph)
    return set(chain.from_iterable(graph[c] for c in max_clique))

def get_colors(s: str) -> List[str]:
    colors = []
    for i, c in enumerate(s):
        colors.append('0' if i in get_max_clique_indices(get_graph(s)) else '1')
    return colors

def is_sorted(s: str) -> bool:
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def is_sorted_after_swap(s: str) -> bool:
    return is_sorted(s) or is_sorted(s[::-1])

colors = get_colors(s)

if is_sorted_after_swap(s):
    print("YES")
    print(''.join(colors))
else:
    print("NO")
