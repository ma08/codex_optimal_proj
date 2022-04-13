#!/usr/bin/env python3
m, n = map(int, input().split())  # row, column
u, l, r, d = map(int, input().split())  # up, left, right, down
puzzle = [list(input()) for _ in range(m)]

for i in range(u):
    print('#' + '.' * (n + l + r) + '#', end='')
    print()
for i in range(m):
    print('#' + '.' * l + ''.join(puzzle[i]) + '.' * r + '#', end='')
    print()
for i in range(d):
    print('#' + '.' * (n + l + r) + '#', end='')
    print()
