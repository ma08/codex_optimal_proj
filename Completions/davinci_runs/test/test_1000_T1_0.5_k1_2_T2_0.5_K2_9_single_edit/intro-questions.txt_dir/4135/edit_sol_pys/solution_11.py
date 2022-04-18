

# n = int(input())
# t = input()

# s = [""] * n

# # reverse the string
# t = t[::-1]

# for i in reversed(range(1, n + 1)):
#     if n % i == 0:
#         # reverse the substring
#         t = t[:i][::-1] + t[i:]

# print(t)

n = int(input())  # no. of rows
m = int(input())  # no. of columns

matrix = [[0 for x in range(m)] for y in range(n)]

for i in range(n):
    for j in range(m):
        print(matrix[i][j])
