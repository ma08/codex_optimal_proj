# https://codeforces.com/contest/1335/problem/D

n, k = map(int, input().split())  # n = len(a)
a = list(map(int, input().split()))  # a = [2, 4, 5, 3, 1]

a = [0] + a  # a = [0, 2, 4, 5, 3, 1]
a.append(n + 1)  # a = [0, 2, 4, 5, 3, 1, 6]

a.sort()

ans = [0] * (n + 2)  # ans = [0, 0, 0, 0, 0, 0, 0]

for i in range(1, n + 2):  # i = 1
    left = a[i - 1] + k  # left = 2 + 2 = 4
    right = a[i] - k - 1  # right = 6 - 2 - 1 = 3
    if left <= right:
        ans[left] += 1  # ans = [0, 0, 0, 1, 1, 0, 0]
        ans[right + 1] -= 1  # ans = [0, 0, 0, 0, 1, 0, 0]

for i in range(1, n + 1):  # i = 1
    ans[i] += ans[i - 1]  # ans = [0, 0, 0, 0, 1, 1, 1]

ans = ans[1:]  # ans = [0, 0, 0, 1, 1, 1]

print(''.join(map(str, ans)))  # 0111
