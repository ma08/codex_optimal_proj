
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.append(0)
a.append(n + 1)

a = sorted(a)

ans = [0] * (n + 1)

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
