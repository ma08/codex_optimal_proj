
#-----Solution-----

n = int(input())
a = list(map(int, input().split()))

#-----Solution 1-----

# a.sort()
#
# max_weight = 0
#
# for i in range(n):
#     if a[i] > max_weight + 1:
#         break
#     max_weight = a[i]
#
# print(i + 1)

#-----Solution 2-----

a.sort()

max_weight = 0

for i in range(n):
    if a[i] > max_weight + 1:
        break
    max_weight = a[i]

print(i + 1)
