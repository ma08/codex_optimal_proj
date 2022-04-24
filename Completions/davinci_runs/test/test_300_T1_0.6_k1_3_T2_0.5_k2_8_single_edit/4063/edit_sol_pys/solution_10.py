
# import sys

# N = int(sys.stdin.readline().rstrip())
# d = list(map(int, sys.stdin.readline().rstrip().split()))

# # print(N)
# # print(d)

# count = 0
# for i in range(1, N):
#     if sum(d[:i]) == sum(d[i:]):
#         count += 1

# print(count)

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)
