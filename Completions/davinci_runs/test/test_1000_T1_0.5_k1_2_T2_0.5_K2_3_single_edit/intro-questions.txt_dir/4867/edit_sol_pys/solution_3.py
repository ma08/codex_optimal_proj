
#http://codeforces.com/problemset/problem/878/A
#Solution

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

print('#' * (l + r + m) + '.' * (d + u))
print('.' * (l + r + m) + '#' * (d + u))
for i in range(m):
    print('#' * l + input() + '#' * r)
print('.' * (l + r + m) + '#' * (d + u))
print('#' * (l + r + m) + '.' * (d + u))
