m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
puzzle = [list(input()) for _ in range(m)]

for i in range(u):
    print('#' + '.' * (n + l + r) + '#') # top
for i in range(m):
    print('#' + '.' * l + ''.join(puzzle[i]) + '.' * r + '#') # middle
for i in range(d):
    print('#' + '.' * (n + l + r) + '#') # bottom
