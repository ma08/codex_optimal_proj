

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

print('#' * (l + r + n) + '.' * (d + u) + '#' * (l + r + n))
print('.' * (l + r + n) + '#' * (d + u) + '.' * (l + r + n))
for i in range(m):
    print('#' * l + input() + '#' * r + '#' * l)
print('.' * (l + r + n) + '#' * (d + u) + '.' * (l + r + n))
print('#' * (l + r + n) + '.' * (d + u) + '#' * (l + r + n))
