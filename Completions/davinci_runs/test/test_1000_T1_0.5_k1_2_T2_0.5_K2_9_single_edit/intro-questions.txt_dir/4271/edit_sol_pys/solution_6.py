

n = int(input())  # number of elements in list
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# print(a)
# print(b)

a.sort()
b.sort()

# for i in range(n):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# for i in range(n):
#     for j in range(n - i - 1):
#         if b[j] > b[j + 1]:
#             b[j], b[j + 1] = b[j + 1], b[j]

# print(a)
# print(b)

count = 0
for i in range(n):
    if a[i] <= b[i]:
        count += 1

print(count)
