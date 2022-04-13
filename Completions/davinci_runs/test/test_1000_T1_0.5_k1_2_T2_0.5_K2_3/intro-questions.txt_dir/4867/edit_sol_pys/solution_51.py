
m, n = map(int, input().split())
up, left, right, down = map(int, input().split())
puzzle = [list(input()) for _ in range(m)]

for i in range(up):
    print('#' + '.' * (n + left + right) + '#')
for i in range(m):
    print('#' + '.' * left + ''.join(puzzle[i]) + '.' * right + '#')
for i in range(down):
    print('#' + '.' * (n + left + right) + '#')
