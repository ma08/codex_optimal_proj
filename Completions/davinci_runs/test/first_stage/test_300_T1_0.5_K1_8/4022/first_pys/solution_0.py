
import sys
sys.stdin = open("input.txt", "r")

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * size
        self.lazy = [0] * size

    def build(self, arr):
        self.build_helper(arr, 0, 0, self.size - 1)

    def build_helper(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_helper(arr, node * 2 + 1, start, mid)
            self.build_helper(arr, node * 2 + 2, mid + 1, end)
            self.tree[node] = max(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def update(self, start, end, val):
        self.update_helper(start, end, val, 0, 0, self.size - 1)

    def update_helper(self, start, end, val, node, node_start, node_end):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if node_start != node_end:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

        if start > node_end or end < node_start:
            return

        if start <= node_start and end >= node_end:
            self.tree[node] += val
            if node_start != node_end:
                self.lazy[node * 2 + 1] += val
                self.lazy[node * 2 + 2] += val
            return

        mid = (node_start + node_end) // 2
        self.update_helper(start, end, val, node * 2 + 1, node_start, mid)
        self.update_helper(start, end, val, node * 2 + 2, mid + 1, node_end)
        self.tree[node] = max(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def query(self, start, end):
        return self.query_helper(start, end, 0, 0, self.size - 1)

    def query_helper(self, start, end, node, node_start, node_end):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if node_start != node_end:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

        if start > node_end or end < node_start:
            return 0

        if start <= node_start and end >= node_end:
            return self.tree[node]

        mid = (node_start + node_end) // 2
        return max(self.query_helper(start, end, node * 2 + 1, node_start, mid),
                   self.query_helper(start, end, node * 2 + 2, mid + 1, node_end))


def main():
    n = int(input())
    segments = []
    for i in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments.sort()

    tree = SegmentTree(n)
    tree.build([0] * n)
    for i in range(n):
        l, r = segments[i]
        tree.update(i, i, r - l)
        if i > 0 and segments[i][0] <= segments[i - 1][1]:
            tree.update(i, i, -1)
        if i < n - 1 and segments[i][1] >= segments[i + 1][0]:
            tree.update(i, i, -1)
    print(tree.query(0, n - 1))


if __name__ == "__main__":
    main()