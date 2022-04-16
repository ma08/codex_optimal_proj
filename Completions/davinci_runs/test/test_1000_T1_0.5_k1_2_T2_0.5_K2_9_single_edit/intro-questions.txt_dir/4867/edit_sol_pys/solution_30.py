import sys

m, n = map(int, input().split())
u, l, r, d = map(int, sys.stdin.readline().split())
puzzle = [list(input()) for _ in range(m)]

for i in range(u):
    print('#' + '.' * (n + l + r) + '#')
for i in range(m):
    print('#' + '.' * l + ''.join(puzzle[i]) + '.' * r + '#')
for i in range(d):
    print('#' + '.' * (n + l + r) + '#')
