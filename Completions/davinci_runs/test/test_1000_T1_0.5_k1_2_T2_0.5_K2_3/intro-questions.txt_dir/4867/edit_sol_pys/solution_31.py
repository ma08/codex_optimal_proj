m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
puzzle = [list(input()) for _ in range(m)]

for _ in range(u):
    print('#' + '.' * (n + l + r) + '#')
for i in range(m):
    print('#' + '.' * l + ''.join(puzzle[i]) + '.' * r + '#')
for _ in range(d):
    print('#' + '.' * (n + l + r) + '#')
