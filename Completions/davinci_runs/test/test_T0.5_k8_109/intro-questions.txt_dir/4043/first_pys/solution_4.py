

import sys
import queue


class Tree:
    def __init__(self, n, d, k):
        self.n = n
        self.d = d
        self.k = k

    def can_construct(self):
        if self.n == 1:
            return True

        if self.d == 1:
            return self.n <= self.k + 1

        if self.d == 2:
            return self.n <= 2 * self.k

        if self.d == 3:
            return self.n <= 2 * self.k + 1

        if self.n == 2:
            return False

        if self.d == self.n - 1:
            return self.n <= 3 * self.k

        if self.n == self.d + 1:
            return self.n <= 3 * self.k + 1

        if self.n == self.d + 2:
            return self.n <= 3 * self.k + 2

        if self.n == self.d + 3:
            return self.n <= 3 * self.k + 3

        if self.n == self.d + 4:
            return self.n <= 3 * self.k + 4

        return False

    def construct(self):
        if not self.can_construct():
            return

        tree = [[] for _ in range(self.n)]

        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if i == j:
                    continue
                if len(tree[i - 1]) < self.k and len(tree[j - 1]) < self.k:
                    tree[i - 1].append(j)
                    tree[j - 1].append(i)

        for i in range(1, self.n + 1):
            for j in tree[i - 1]:
                print(i, j)

    def is_diameter(self, tree):
        q = queue.Queue()
        visited = [False] * self.n
        dist = [0] * self.n

        q.put(0)
        visited[0] = True

        while not q.empty():
            v = q.get()
            for u in tree[v]:
                if not visited[u]:
                    visited[u] = True
                    dist[u] = dist[v] + 1
                    q.put(u)

        return max(dist) == self.d

    def is_tree(self, tree):
        if self.n == 1:
            return True

        visited = [False] * self.n
        q = queue.Queue()

        visited[0] = True
        q.put(0)

        while not q.empty():
            v = q.get()
            for u in tree[v]:
                if not visited[u]:
                    visited[u] = True
                    q.put(u)

        return all(visited)

    def construct2(self):
        if not self.can_construct():
            return

        tree = [[] for _ in range(self.n)]

        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if i == j:
                    continue
                if len(tree[i - 1]) < self.k and len(tree[j - 1]) < self.k:
                    tree[i - 1].append(j - 1)
                    tree[j - 1].append(i - 1)

        if not self.is_diameter(tree):
            return

        if not self.is_tree(tree):
            return

        for i in range(1, self.n + 1):
            for j in tree[i - 1]:
                print(i, j + 1)


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, d, k = next(reader)
    tree = Tree(n, d, k)
    tree.construct2()


if __name__ == "__main__":
    main()