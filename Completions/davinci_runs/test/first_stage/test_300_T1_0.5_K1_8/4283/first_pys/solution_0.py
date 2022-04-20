

n = int(input())
a = list(map(int, input().split()))
a.sort()

# O(n^2) solution
# def check(x):
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if abs(a[i] - a[j]) <= x:
#                 return True
#     return False

# l = 0
# r = 10**9
# while l < r:
#     m = (l + r) // 2
#     if check(m):
#         l = m + 1
#     else:
#         r = m
# print(l - 1)

# O(n) solution
cnt = 0
for i in range(1, n):
    if abs(a[i] - a[i - 1]) <= 5:
        cnt += 1
print(cnt + 1)