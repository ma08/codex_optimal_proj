
# h, w = map(int, input().split())
# grid = []
# for i in range(h):
#     grid.append(list(input()))

# # print("grid: ")
# # print(grid)

# # check for columns
# for i in range(h):
#     all_white = True
#     for j in range(w):
#         if grid[i][j] == '#':
#             all_white = False
#             break
#     if all_white:
#         # print("col: " + str(i))
#         grid.pop(i)
#         h -= 1
#         i -= 1

# # print("grid: ")
# # print(grid)

# # check for rows
# for j in range(w):
#     all_white = True
#     for i in range(h):
#         if grid[i][j] == '#':
#             all_white = False
#             break
#     if all_white:
#         # print("col: " + str(j))
#         for i in range(h):
#             grid[i].pop(j)
#         w -= 1
#         j -= 1

# # print("grid: ")
# # print(grid)

# for i in range(h):
#     print("".join(grid[i]))

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     a.sort()
#     # print(a)
#     d = 0
#     for i in range(1, n):
#         d += max(0, k - a[i] + a[i-1])
#     print(d)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     # print(a)
#     a.sort()
#     # print(a)
#     d = 0
#     for i in range(1, n):
#         d += abs(a[i]-a[i-1]) - 1
#     print(d)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     a.sort()
#     # print(a)
#     d = 0
#     for i in range(1, n):
#         if a[i] <= a[i-1]:
#             d += a[i-1] - a[i] + 1
#             a[i] = a[i-1] + 1
#     print(d)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    d = 0
    for i in range(1, n):
        if a[i] <= a[i-1]:
            d += a[i-1] - a[i] + 1
            a[i] = a[i-1] + 1
    print(d)
