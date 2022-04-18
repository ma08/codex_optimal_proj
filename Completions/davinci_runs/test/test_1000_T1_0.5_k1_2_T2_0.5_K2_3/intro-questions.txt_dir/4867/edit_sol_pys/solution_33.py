
m, n = map(int, input().split())  # row, column
u, l, r, d = map(int, input().split())  # up, left, right, down
puzzle = [list(input()) for _ in range(n)]

for i in range(u):
    print('#' + '.' * (n + l + r) + '#')
for i in range(m):
    print('#' + '.' * l + ''.join(puzzle[i]) + '.' * r + '#')
for i in range(d):
    print('#' + '.' * (n + l + r) + '#')
