

# n, k, x = map(int, input().split())
# pictures = list(map(int, input().split()))

# # print(n, k, x)
# # print(pictures)

# # dp[i][j] = max sum of pictures from range [i, j]
# # with j - i >= k
# dp = [[0 for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     dp[i][i] = pictures[i]

# for width in range(1, n):
#     for i in range(n - width):
#         j = i + width
#         if j - i + 1 < k:
#             dp[i][j] = 0
#         else:
#             dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], dp[i][j - 1] + pictures[j])

# # for row in dp:
# #     print(row)

# if x == n:
#     print(dp[0][n - 1])
# elif x > n:
#     print(-1)
# else:
#     # dp[i][j] = max sum of pictures from range [i, j]
#     # with j - i >= k and j - i >= x
#     dp2 = [[0 for _ in range(n)] for _ in range(n)]

#     for i in range(n):
#         dp2[i][i] = pictures[i]

#     for width in range(1, n):
#         for i in range(n - width):
#             j = i + width
#             if j - i + 1 < k or j - i + 1 < x:
#                 dp2[i][j] = 0
#             else:
#                 dp2[i][j] = max(dp2[i][j - 1], dp2[i + 1][j], dp2[i][j - 1] + pictures[j])

#     # for row in dp2:
#     #     print(row)

#     print(dp2[0][n - 1])


def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i == len(a):
        result += b[j:]
    else:
        result += a[i:]
    return result


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(a, 2))
