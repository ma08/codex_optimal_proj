
from collections import defaultdict

def find_cycle(graph, start):
    visited, cycle = set(), [start]
    while True:
        if cycle[-1] in visited:
            return cycle[cycle.index(cycle[-1]):]
        else:
            visited.add(cycle[-1])
            cycle.append(graph[cycle[-1]])

def find_all_cycles(graph):
    cycles = []
    visited = set()
    for start in graph:
        if start not in visited:
            cycle = find_cycle(graph, start)
            cycles.append(cycle)
            visited |= set(cycle)
    return cycles

def solve(input):
    kids = defaultdict(set)
    for i in range(len(input)):
        kids[input[i][0]].add(i+1)
        kids[input[i][1]].add(i+1)
    cycles = find_all_cycles(kids)
    res = []
    for cycle in cycles:
        res.append(cycle[0])
        for i in range(1, len(cycle)):
            res.append(kids[cycle[i-1]].difference(set([cycle[i]])).pop())
    return res
