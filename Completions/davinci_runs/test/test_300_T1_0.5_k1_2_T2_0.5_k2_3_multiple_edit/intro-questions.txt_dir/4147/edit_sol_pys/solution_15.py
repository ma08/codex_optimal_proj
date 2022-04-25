# ABC081A

N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c):
    if a == A and b == B and c == C:
        return 0
    if cur == N:
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c))
    res = min(res, dfs(cur + 1, a + ls[cur], b, c) + 10)
    res = min(res, dfs(cur + 1, a, b + ls[cur], c) + 10)
    res = min(res, dfs(cur + 1, a, b, c + ls[cur]) + 10)
    if ls[cur] > 1:
        res = min(res, dfs(cur + 1, a + ls[cur] - 1, b, c) + 9)
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 1, c) + 9)
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 1) + 9)
    if ls[cur] > 2:
        res = min(res, dfs(cur + 1, a + ls[cur] - 2, b, c) + 8)
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 2, c) + 8)
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 2) + 8)
    return res

print(dfs(0, 0, 0, 0))

# ABC087B
A = int(input())
B = int(input())
C = int(input())
X = int(input())

res = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            if a * 500 + b * 100 + c * 50 == X:
                res += 1
print(res)

# ABC087C
n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

res = 0
for i in range(n):
    res = max(res, sum(a1[:i + 1]) + sum(a2[i:]))
print(res)

# ABC088B
N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = sum(a[::2])
bob = sum(a[1::2])
print(alice - bob)

# ABC085B
N = int(input())
d = [int(input()) for _ in range(N)]
print(len(set(d)))

# ABC085C
N, Y = map(int, input().split())

for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if z < 0:
            continue
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            exit()
print(-1, -1, -1)

# ABC086C
N = int(input())
t = [0]
x = [0]
y = [0]
for _ in range(N):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)

for i in range(N):
    dt = t[i + 1] - t[i]
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if dt < dist:
        print('No')
        exit()
    if dist % 2 != dt % 2:
        print('No')
        exit()
print('Yes')

# ABC085C
N, Y = map(int, input().split())

for x in range(N + 1):
    for y in range(N + 1):
        z = N - x - y
        if z < 0:
            continue
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            exit()
print(-1, -1, -1)
