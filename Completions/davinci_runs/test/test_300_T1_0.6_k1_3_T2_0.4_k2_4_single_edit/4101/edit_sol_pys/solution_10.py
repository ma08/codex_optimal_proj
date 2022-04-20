import sys
from collections import deque
from copy import deepcopy



class Node:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.c)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.c == other.c

    def __hash__(self):
        return hash(str(self))


def bfs(start, end):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    while q:
        cur = q.popleft()
        if cur == end:
            return True
        for next in get_next(cur):
            if next not in visited:
                q.append(next)
                visited.add(next)
    return False


def get_next(node):
    x, y, c = node.x, node.y, node.c
    res = []
    if x > 0 and a[x-1][y] == c:
        res.append(Node(x-1, y, c))
    if x < n-1 and a[x+1][y] == c:
        res.append(Node(x+1, y, c))
    if y > 0 and a[x][y-1] == c:
        res.append(Node(x, y-1, c))
    if y < m-1 and a[x][y+1] == c:
        res.append(Node(x, y+1, c))
    return res


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m


def get_next_color(c):
    return 1 - c


def is_valid_color(x, y, c):
    if not is_valid(x, y):
        return False
    if a[x][y] == c:
        return True
    return False


def get_next_color_node(node):
    x, y, c = node.x, node.y, node.c
    res = []
    if is_valid_color(x-1, y, get_next_color(c)):
        res.append(Node(x-1, y, get_next_color(c)))
    if is_valid_color(x+1, y, get_next_color(c)):
        res.append(Node(x+1, y, get_next_color(c)))
    if is_valid_color(x, y-1, get_next_color(c)):
        res.append(Node(x, y-1, get_next_color(c)))
    if is_valid_color(x, y+1, get_next_color(c)):
        res.append(Node(x, y+1, get_next_color(c)))
    return res


def is_connected():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                start = Node(i, j, 1)
                end = Node(i, j, 0)
                return bfs(start, end)
    return True


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    global a
    global n
    global m
    a = [[0]*m for _ in range(n)]
    for i in range(n):
        a[i] = [int(x) for x in sys.stdin.readline().split()]

    if not is_connected():
        print("NO")
        return

    r = [0] * n
    c = [0] * m

    for i in range(n):
        zero = 0
        one = 0
        for j in range(m):
            if a[i][j] == 0:
                zero += 1
            else:
                one += 1
        if zero > one:
            r[i] = 1

    for j in range(m):
        zero = 0
        one = 0
        for i in range(n):
            if a[i][j] == 0:
                zero += 1
            else:
                one += 1
        if zero > one:
            c[j] = 1

    for i in range(n):
        for j in range(m):
            if r[i] == 1:
                a[i][j] = 1 - a[i][j]
            if c[j] == 1:
                a[i][j] = 1 - a[i][j]

    sorted_r = True
    for i in range(n):
        for j in range(m - 1):
            if a[i][j] > a[i][j+1]:
                sorted_r = False

    sorted_c = True
    for j in range(m):
        for i in range(n - 1):
            if a[i][j] > a[i + 1][j]:
                sorted_c = False

    if sorted_r and sorted_c:
        print("YES")
        print("".join([str(x) for x in r]))

        print("".join([str(x) for x in c]))
    else:
        print("NO")

if __name__ == '__main__':
    main()
