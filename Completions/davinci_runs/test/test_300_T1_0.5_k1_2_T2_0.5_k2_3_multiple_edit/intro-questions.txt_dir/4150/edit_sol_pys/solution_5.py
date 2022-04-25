
# input
n, k = map(int, input().split())

# array
a = list(map(int, input().split()))

# a = [2, 4, 5, 3, 1]
# n = len(a)
# k = 2

# add 0 and n + 1
a = [0] + a
a.append(n + 1)

# sort
a.sort()

# initialize
ans = [0] * (n + 2)

# calculate
for i in range(1, n + 2):
    left = a[i - 1] + k
    right = a[i] - k - 1
    if left <= right:
        ans[left] += 1
        ans[right + 1] -= 1

# calculate
for i in range(1, n + 1):
    ans[i] += ans[i - 1]

# remove 0
ans = ans[1:]

# output
print(''.join(map(str, ans)))
