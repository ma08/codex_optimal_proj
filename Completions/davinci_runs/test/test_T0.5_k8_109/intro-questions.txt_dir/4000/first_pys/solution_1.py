

from collections import defaultdict
from sys import stdin, stdout

class Node:
    def __init__(self, number):
        self.number = number
        self.adj = []
        self.parent = None
        self.depth = 0
        self.size = 1
        self.heavy_child = None


def dfs(node):
    for child in node.adj:
        if child.number != node.parent:
            child.parent = node.number
            child.depth = node.depth + 1
            dfs(child)
            node.size += child.size
            if node.heavy_child is None or child.size > node.heavy_child.size:
                node.heavy_child = child


def dfs2(node, chain_head):
    node.head = chain_head
    if node.heavy_child is not None:
        dfs2(node.heavy_child, chain_head)
    for child in node.adj:
        if child.number != node.parent and child.number != node.heavy_child:
            dfs2(child, child.number)


def get_lca(node1, node2):
    while node1.head != node2.head:
        if node1.depth > node2.depth:
            node1 = nodes[node1.head]
        else:
            node2 = nodes[node2.head]
    if node1.depth > node2.depth:
        return node2.number
    else:
        return node1.number


def get_max_path(node1, node2):
    ans = 0
    while node1.head != node2.head:
        if node1.depth > node2.depth:
            ans = max(ans, node1.size - nodes[node1.head].size)
            node1 = nodes[node1.head]
        else:
            ans = max(ans, node2.size - nodes[node2.head].size)
            node2 = nodes[node2.head]
    if node1.depth > node2.depth:
        ans = max(ans, node2.size - node1.size)
    else:
        ans = max(ans, node1.size - node2.size)
    return ans


n = int(stdin.readline())
nodes = [Node(i) for i in range(1, n + 1)]
for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    nodes[a].adj.append(nodes[b])
    nodes[b].adj.append(nodes[a])

dfs(nodes[1])
dfs2(nodes[1], 1)

best_ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        lca = get_lca(nodes[i], nodes[j])
        best_ans = max(best_ans, get_max_path(nodes[lca], nodes[i]) + get_max_path(nodes[lca], nodes[j]) + 1)

stdout.write(f'{best_ans}\n')

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        lca = get_lca(nodes[i], nodes[j])
        if best_ans == get_max_path(nodes[lca], nodes[i]) + get_max_path(nodes[lca], nodes[j]) + 1:
            stdout.write(f'{i} {j} {lca}\n')
            exit()