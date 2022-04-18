from collections import defaultdict


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def same(x, y):
    return find(x) == find(y)


n, k = map(int, input().split())
p = list(map(int, input().split()))

# a = [2, 4, 5, 3, 1]
# n = len(a)
# k = 2

a = [0] + a
a.append(n + 1)

a.sort()

ans = [0] * (n + 2)

for i in range(1, n + 2):
    left = a[i - 1] + k
    right = a[i] - k - 1
    if left <= right:
        ans[left] += 1
        ans[right + 1] -= 1

for i in range(1, n + 1):
    ans[i] += ans[i - 1]

ans = ans[1:]

print(''.join(map(str, ans)))
