
# n = int(input())
# p = [int(x) for x in input().split()]
#
# count = 0
# for i in range(1, n - 1):
#     if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
#         count += 1
#
# print(count)

n = int(input())
l = [int(x) for x in input().split()]

l2 = []
for i in range(n):
    if i == 0:
        l2.append(l[i])
    else:
        l2.append(l[i] + l2[i - 1])

print(l2)

# l = [1, 2, 3, 4, 5]
# l2 = []
# for i in range(len(l)):
#     if i == 0:
#         l2.append(l[i])
#     else:
#         l2.append(l[i] + l2[i - 1])
#
# print(l2)
