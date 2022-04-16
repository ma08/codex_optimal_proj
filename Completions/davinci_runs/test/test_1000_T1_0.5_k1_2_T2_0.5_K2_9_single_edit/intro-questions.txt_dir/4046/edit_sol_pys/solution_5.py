#!/usr/bin/env python3

from collections import defaultdict
import sys

def get_input():
    n, m = map(int, input().split())
    return n, m

def create_graph(n, m):
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    return g

def create_order(g, n):
    order = []
    seen = [False] * n
    for i in range(n):
        if seen[i]:
            continue
        stack = [i]
        while stack:
            j = stack.pop()
            if seen[j]:
                continue
            seen[j] = True
            order.append(j)
            for k in g[j]:
                if not seen[k]:
                    stack.append(k)
    return order

def print_order(order):
    print(" ".join(map(str, order)))

def main():
    n, m = get_input()
    g = create_graph(n, m)
    order = create_order(g, n)
    print_order(order)

if __name__ == "__main__":
    main()
