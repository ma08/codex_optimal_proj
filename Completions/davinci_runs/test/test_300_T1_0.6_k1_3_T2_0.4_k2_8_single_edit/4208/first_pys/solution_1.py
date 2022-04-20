

import sys
import math

class Node:
    def __init__(self, data, parent, left=None, right=None, level=0):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.level = level
        self.type = None
        self.start = None
        self.end = None
        self.inorder = None
        self.postorder = None
        self.preorder = None
        self.subtree_size = None

    def __repr__(self):
        return "{}".format(self.data)


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.nodes = {}
        self.root = None
        self.start = None
        self.end = None
        self.inorder_index = 0
        self.postorder_index = 0
        self.preorder_index = 0
        self.subtree_size = 0

    def construct_tree(self, root_id=1):
        for i in range(1, self.n + 1):
            self.nodes[i] = Node(i, None, None, None, None)

        for edge in self.edges:
            parent, child = edge
            parent_node = self.nodes[parent]
            child_node = self.nodes[child]
            child_node.parent = parent_node
            if parent_node.left is None:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        self.root = self.nodes[root_id]

    def set_level(self, node):
        if node.left is None and node.right is None:
            node.level = 0
        else:
            if node.left is not None:
                node.level = node.left.level + 1
            if node.right is not None:
                node.level = max(node.level, node.right.level + 1)

    def set_type(self, node):
        if node.left is not None and node.right is not None:
            node.type = "internal"
        elif node.left is None and node.right is None:
            node.type = "leaf"
        else:
            node.type = "external"

    def set_start_end(self, node):
        node.start = self.start
        self.start += 1
        if node.left is not None:
            self.set_start_end(node.left)
        node.end = self.start
        if node.right is not None:
            self.set_start_end(node.right)

    def set_subtree_size(self, node):
        node.subtree_size = 1
        if node.left is not None:
            node.subtree_size += self.set_subtree_size(node.left)
        if node.right is not None:
            node.subtree_size += self.set_subtree_size(node.right)
        return node.subtree_size

    def set_inorder(self, node):
        if node.left is not None:
            self.set_inorder(node.left)
        node.inorder = self.inorder_index
        self.inorder_index += 1
        if node.right is not None:
            self.set_inorder(node.right)

    def set_postorder(self, node):
        if node.left is not None:
            self.set_postorder(node.left)
        if node.right is not None:
            self.set_postorder(node.right)
        node.postorder = self.postorder_index
        self.postorder_index += 1

    def set_preorder(self, node):
        node.preorder = self.preorder_index
        self.preorder_index += 1
        if node.left is not None:
            self.set_preorder(node.left)
        if node.right is not None:
            self.set_preorder(node.right)

    def setup(self):
        self.start = 1
        self.end = 1
        self.inorder_index = 1
        self.postorder_index = 1
        self.preorder_index = 1
        self.subtree_size = 0

        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            self.set_level(node)
            self.set_type(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        self.set_start_end(self.root)
        self.set_subtree_size(self.root)
        self.set_inorder(self.root)
        self.set_postorder(self.root)
        self.set_preorder(self.root)

    def __repr__(self):
        graph_string = ""
        for i in range(1, self.n + 1):
            node = self.nodes[i]
            graph_string += "{} {} {} {} {} {} {} {}\n".format(
                node.data, node.parent.data if node.parent is not None else None, node.left.data if node.left is not None else None,
                node.right.data if node.right is not None else None, node.level, node.type, node.start, node.end)
        return graph_string


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.segment = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def build(self, node, start, end):
        if start == end:
            self.segment[node] = 0
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.segment[node] = self.segment[2 * node] + self.segment[2 * node + 1]

    def update(self, node, start, end, l, r):
        if self.lazy[node] != 0:
            self.segment[node] = (end - start + 1) - self.segment[node]
            if start != end:
                self.lazy[2 * node] ^= 1
                self.lazy[2 * node + 1] ^= 1
            self.lazy[node] = 0

        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.segment[node] = (end - start + 1) - self.segment[node]
            if start != end:
                self.lazy[2 * node] ^= 1
                self.lazy[2 * node + 1] ^= 1
            return

        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r)
        self.update(2 * node + 1, mid + 1, end, l, r)
        self.segment[node] = self.segment[2 * node] + self.segment[2 * node + 1]

    def query(self, node, start, end, l, r):
        if self.lazy[node] != 0:
            self.segment[node] = (end - start + 1) - self.segment[node]
            if start != end:
                self.lazy[2 * node] ^= 1
                self.lazy[2 * node + 1] ^= 1
            self.lazy[node] = 0

        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.segment[node]

        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result


def is_possible(segment_tree, graph, i, j):
    # if graph.nodes[i].level % 2 == graph.nodes[j].level % 2:
    #     return False

    # if graph.nodes[i].level % 2 == 0:
    #     left = graph.nodes[i].start
    #     right = graph.nodes[j].start
    # else:
    #     left = graph.nodes[j].start
    #     right = graph.nodes[i].start

    # if left > right:
    #     left, right = right, left

    # if segment_tree.query(1, 1, graph.n, left, right) > 0:
    #     return False

    # return True

    return graph.nodes[i].start > graph.nodes[j].start


def main():
    n = int(input())
    l = input()
    r = input()

    l_list = []
    r_list = []
    for i in range(n):
        if l[i] != '?':
            l_list.append(l[i])
        if r[i] != '?':
            r_list.append(r[i])

    l_list = list(set(l_list))
    r_list = list(set(r_list))

    if len(l_list) > len(r_list):
        l_list, r_list = r_list, l_list

    pairs = []

    if len(l_list) == 0:
        for i in range(n):
            for j in range(n):
                if i != j:
                    pairs.append((i, j))
        print(len(pairs))
        for pair in pairs:
            print("{} {}".format(pair[0] + 1, pair[1] + 1))
        return

    l_to_index = {}
    r_to_index = {}

    for i in range(len(l_list)):
        l_to_index[l_list[i]] = i + 1
    for i in range(len(r_list)):
        r_to_index[r_list[i]] = i + 1

    edges = []
    for i in range(len(r_list)):
        edges.append((r_to_index[r_list[i]], i + 1))

    graph = Graph(len(r_list), edges)
    graph.construct_tree()
    graph.setup()

    segment_tree = SegmentTree(graph.n)
    segment_tree.build(1, 1, graph.n)

    # segment_tree.update(1, 1, graph.n, graph.nodes[1].start, graph.nodes[1].end)

    for i in range(len(l_list)):
        l_index = l_to_index[l_list[i]]
        for j in range(graph.n):
            r_index = j + 1
            if l_index == r_index:
                continue
            if is_possible(segment_tree, graph, l_index, r_index):
                pairs.append((i, j))
                segment_tree.update(1, 1, graph.n, graph.nodes[r_index].start, graph.nodes[r_index].end)

    # print(graph)
    # print(l_to_index)
    # print(r_to_index)
    # print(segment_tree.segment)
    # print(segment_tree.lazy)

    print(len(pairs))
    for pair in pairs:
        print("{} {}".format(pair[0] + 1, pair[1] + 1))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()