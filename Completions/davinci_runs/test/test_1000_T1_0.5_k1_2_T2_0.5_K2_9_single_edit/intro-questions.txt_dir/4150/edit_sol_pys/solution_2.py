
n, k = map(int, input().split())
a = list(map(int, input().split()))

# a = [2, 4, 5, 3, 1]
# n = len(a)
# k = 2

# a = [0] + a
# a.append(n + 1)

# a.sort()

ans = [0] * (n + 1)

for i in range(n):
    left = max(a[i] - k, 0)
    right = min(a[i] + k + 1, n)
    ans[left] += 1
    ans[right] -= 1

for i in range(1, n + 1):
    ans[i] += ans[i - 1]

# ans = ans[1:]

print(' '.join(map(str, ans)))
