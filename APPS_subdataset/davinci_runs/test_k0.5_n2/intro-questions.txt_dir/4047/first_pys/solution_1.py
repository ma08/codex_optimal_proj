

n = int(input())
x = list(map(int, input().split()))

# if n == 1:
#     print(0)
#     exit()

# x.sort()
# m = x[0]
# c = 0
# for i in range(1, n):
#     c += abs(m - x[i])

# print(c)

# if n == 1:
#     print(0)
#     exit()

# x.sort()
# m = x[0]
# c = 0
# for i in range(1, n):
#     c += abs(m - x[i])

# print(c)

x.sort()
c = 0
for i in range(1, n):
    c += abs(x[i] - x[i - 1])

print(c)