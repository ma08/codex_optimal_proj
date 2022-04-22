import math

# https://codeforces.com/problemset/problem/1324/B


n, k = map(int, input().split())
a = list(map(int, input().strip().split()))

# a = [2, 4, 5, 3, 1]
# n = len(a)
# k = 2

a = [0] + a + [n + 1]

a.sort(reverse=True)

ans = [0] * (n + 2)

    # print(i, a[i])
    left = a[i - 1] + k
    # print(left, right)
    right = a[i] - k - 1
    if left <= right:
        ans[left + 1] += 1
        ans[right + 1] -= 1

for i in range(1, n + 2):
    ans[i] += ans[i - 1]

ans = ans[1:]

print(''.join(map(str, ans)))
