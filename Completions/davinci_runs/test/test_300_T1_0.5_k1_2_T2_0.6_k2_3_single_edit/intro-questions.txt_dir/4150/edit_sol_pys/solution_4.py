

n, k = map(int, input().split())
a = list(map(int, input().split()))

# a = [2, 4, 5, 3, 1]
# n = len(a)
# k = 2

a = [0] + a  # [0, 2, 4, 5, 3, 1]
a.append(n + 1)

a.sort()

ans = [0] * (n + 2)

for i in range(1, n + 2):  # i = 1, 2, 3, 4, 5, 6
    # left = 0+2, 2+2, 4+2, 5+2, 3+2, 1+2
    # right = 2-2-1, 4-2-1, 5-2-1, 3-2-1, 1-2-1
    left = a[i - 1] + k
    right = a[i] - k - 1
    if left <= right:
        ans[left] += 1
        ans[right + 1] -= 1

for i in range(1, n + 1):
    ans[i] += ans[i - 1]

ans = ans[1:]

print(''.join(map(str, ans)))
