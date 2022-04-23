
from collections import defaultdict
from sys import stdin, stdout
from itertools import chain, combinations

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

def get_max_clique_size(graph):
    # https://en.wikipedia.org/wiki/Clique_problem
    def get_max_clique_size_recursive(graph, size=0):
        if not graph:
            return size
        v = next(iter(graph))
        return max(get_max_clique_size_recursive(graph - {v} - n, size) for n in graph[v])

    max_clique = set()
    bron_kerbosch(set(), set(graph.keys()), set())
    return max_clique

def get_max_clique_size(graph):
    return len(get_max_clique(graph))

def get_max_clique_indices(graph):
    max_clique = get_max_clique(graph)
    return set(chain.from_iterable(graph[c] for c in max_clique))

def get_colors(s):
    colors = []
    for i, c in enumerate(s):
        colors.append('0' if i in get_max_clique_indices(get_graph(s)) else '1')
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
