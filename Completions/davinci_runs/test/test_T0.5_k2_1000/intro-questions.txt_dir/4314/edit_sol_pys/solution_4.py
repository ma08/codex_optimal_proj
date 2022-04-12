# https://atcoder.jp/contests/abc086/tasks/abc086_a

# h, w = map(int, input().split())
# grid = []
# for i in range(h):
#     grid.append(list(input()))

# # print("grid: ")
# # print(grid)

# # check for rows
# for i in range(h):
#     all_black = True
#     for j in range(w):
#         if grid[i][j] == '#':
#             all_black = False
#             break
#     if all_black:
#         # print("row: " + str(i))
#         grid.pop(i)
#         h -= 1
#         i -= 1

# # print("grid: ")
# # print(grid)

# # check for columns
# for j in range(w):
#     all_black = True
#     for i in range(h):
#         if grid[i][j] == '#':
#             all_black = False
#             break
#     if all_black:
#         # print("col: " + str(j))
#         for i in range(h):
#             grid[i].pop(j)
#         w -= 1
#         j -= 1

# # print("grid: ")
# # print(grid)

# for i in range(h):
#     print("".join(grid[i]))

s = input()
t = input()

if s == t:
    print("same")
elif s.lower() == t.lower():
    print("case-insensitive")
else:
    print("different")
