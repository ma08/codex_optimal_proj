"""
A - Biscuit Generator
https://atcoder.jp/contests/abc138/tasks/abc138_a
"""

a = int(input())
s = input()

if a >= 3200:
    print(s)
else:
    print('red')




"""
B - Resale
https://atcoder.jp/contests/abc138/tasks/abc138_b
"""

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += 1 / a

print(1 / ans)

"""
C - Alchemist
https://atcoder.jp/contests/abc138/tasks/abc138_c
"""

N = int(input())
v = list(map(int, input().split()))

v.sort()

for i in range(1, N):
    v[i] = (v[i] + v[i - 1]) / 2

print(v[-1])

"""
D - Ki
https://atcoder.jp/contests/abc138/tasks/abc138_d
"""

N, Q = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

X = [0] * (N + 1)
for _ in range(Q):
    p, x = map(int, input().split())
    X[p] += x

ans = [0] * (N + 1)
stack = [1]
while stack:
    node = stack.pop()
    ans[node] += X[node]
    for child in tree[node]:
        if child == node:
            continue
        ans[child] += ans[node]
        stack.append(child)

print(' '.join(map(str, ans[1:])))

"""
E - Powerful Discount Tickets
https://atcoder.jp/contests/abc138/tasks/abc138_e
"""

S = input()
T = input()

ans = -1
for i in range(len(T)):
    if T[i] in S:
        index = S.index(T[i])
        S = S[index + 1:] + S[:index + 1]
        if S == T:
            ans = i + 1
            break

print(ans)

"""
F - Div Rem
https://atcoder.jp/contests/abc138/tasks/abc138_f
"""

N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7

ans = 0
for i in range(N):
    ans += (A[i] * pow(2, i, mod)) % mod
    ans %= mod

print(ans)
N = int(input())
W = list(map(int, input().split()))
