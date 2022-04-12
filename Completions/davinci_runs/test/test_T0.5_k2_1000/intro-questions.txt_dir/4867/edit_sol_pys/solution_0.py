
# Solution

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

print('#' * (l + r + n) + '.' * (d + u + n))
print('.' * (l + r + n) + '#' * (d + u + n))
for i in range(m):
    print('#' * l + input() + '#' * r)
print('.' * (l + r + n) + '#' * (d + u + n))
print('#' * (l + r + n) + '.' * (d + u + n))
