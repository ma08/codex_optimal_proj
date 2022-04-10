

import sys

def read_ints():
    temp = input().split()
    temp = [int(t) for t in temp]
    return temp

def read_int():
    temp = read_ints()
    return temp[0]

class Node():
    def __init__(self, val):
        self.val = val
        self.adj = []
        self.visited = False
        self.parent = None
        self.children = []
        self.depth = 0
        self.subtree_size = 1
        self.max_subtree_size = 0
        self.max_subtree_size_node = self

    def add_adj(self, node):
        self.adj.append(node)

def dfs(root):
    root.visited = True
    for node in root.adj:
        if not node.visited:
            node.parent = root
            node.depth = root.depth + 1
            dfs(node)
            root.subtree_size += node.subtree_size
            if node.subtree_size > root.max_subtree_size:
                root.max_subtree_size = node.subtree_size
                root.max_subtree_size_node = node
            elif node.max_subtree_size > root.max_subtree_size:
                root.max_subtree_size = node.max_subtree_size
                root.max_subtree_size_node = node.max_subtree_size_node

def get_max_subtree_size_node(root):
    max_subtree_size = 0
    max_subtree_size_node = None
    for node in root.adj:
        if node.visited:
            continue
        if node.subtree_size > max_subtree_size:
            max_subtree_size = node.subtree_size
            max_subtree_size_node = node
        elif node.max_subtree_size > max_subtree_size:
            max_subtree_size = node.max_subtree_size
            max_subtree_size_node = node.max_subtree_size_node
    return max_subtree_size_node

def get_max_subtree_size(root):
    max_subtree_size = 0
    for node in root.adj:
        if node.visited:
            continue
        if node.subtree_size > max_subtree_size:
            max_subtree_size = node.subtree_size
        elif node.max_subtree_size > max_subtree_size:
            max_subtree_size = node.max_subtree_size
    return max_subtree_size

def find_centroid(root):
    dfs(root)
    while True:
        max_subtree_size_node = get_max_subtree_size_node(root)
        max_subtree_size = get_max_subtree_size(root)
        if max_subtree_size <= root.subtree_size // 2:
            return root
        root = max_subtree_size_node

def get_max_subtree_size_at_depth(node, depth):
    max_subtree_size = 0
    for child in node.children:
        if child.depth == depth:
            max_subtree_size = max(max_subtree_size, child.subtree_size)
        else:
            max_subtree_size = max(max_subtree_size, get_max_subtree_size_at_depth(child, depth))
    return max_subtree_size

def find_max_subtree_size_at_depth(node, depth):
    max_subtree_size = 0
    max_subtree_size_node = None
    for child in node.children:
        if child.depth == depth:
            if child.subtree_size > max_subtree_size:
                max_subtree_size = child.subtree_size
                max_subtree_size_node = child
        else:
            subtree_size, subtree_size_node = find_max_subtree_size_at_depth(child, depth)
            if subtree_size > max_subtree_size:
                max_subtree_size = subtree_size
                max_subtree_size_node = subtree_size_node
    return max_subtree_size, max_subtree_size_node

def get_max_subtree_size_at_depth_from_subtree(node, depth):
    max_subtree_size = 0
    for child in node.children:
        if child.depth == depth:
            max_subtree_size = max(max_subtree_size, child.subtree_size)
        else:
            max_subtree_size = max(max_subtree_size, get_max_subtree_size_at_depth_from_subtree(child, depth))
    return max_subtree_size

def find_max_subtree_size_at_depth_from_subtree(node, depth):
    max_subtree_size = 0
    max_subtree_size_node = None
    for child in node.children:
        if child.depth == depth:
            if child.subtree_size > max_subtree_size:
                max_subtree_size = child.subtree_size
                max_subtree_size_node = child
        else:
            subtree_size, subtree_size_node = find_max_subtree_size_at_depth_from_subtree(child, depth)
            if subtree_size > max_subtree_size:
                max_subtree_size = subtree_size
                max_subtree_size_node = subtree_size_node
    return max_subtree_size, max_subtree_size_node

def solve(root):
    centroid = find_centroid(root)
    centroid.visited = False
    for node in centroid.adj:
        if not node.visited:
            node.parent = centroid
            node.depth = centroid.depth + 1
            centroid.children.append(node)
    if len(centroid.children) == 0:
        return 0, [centroid.val]
    elif len(centroid.children) == 1:
        return 1, [centroid.val, centroid.children[0].val]
    else:
        max_subtree_size_1, max_subtree_size_node_1 = find_max_subtree_size_at_depth(centroid, centroid.children[0].depth)
        max_subtree_size_2, max_subtree_size_node_2 = find_max_subtree_size_at_depth(centroid, centroid.children[1].depth)
        max_subtree_size_3, max_subtree_size_node_3 = find_max_subtree_size_at_depth_from_subtree(centroid, centroid.children[0].depth)
        max_subtree_size_4, max_subtree_size_node_4 = find_max_subtree_size_at_depth_from_subtree(centroid, centroid.children[1].depth)
        if max_subtree_size_1 + max_subtree_size_2 > max_subtree_size_3 + max_subtree_size_4:
            return max_subtree_size_1 + max_subtree_size_2, [centroid.val, max_subtree_size_node_1.val, max_subtree_size_node_2.val]
        else:
            return max_subtree_size_3 + max_subtree_size_4, [centroid.val, max_subtree_size_node_3.val, max_subtree_size_node_4.val]

n = read_int()
nodes = [None] + [Node(i) for i in range(1, n + 1)]
for _ in range(n - 1):
    a, b = read_ints()
    nodes[a].add_adj(nodes[b])
    nodes[b].add_adj(nodes[a])
res, ans = solve(nodes[1])
print(res)
print(*ans)