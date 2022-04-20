

#-----Solution-----

n, m = [int(i) for i in input().split()]

nums = [False for i in range(m + 1)]

for i in range(n):
    l, r = [int(i) for i in input().split()]
    for j in range(l, r + 1):
        nums[j] = True

c = 0

for i in range(1, m + 1):
    if not nums[i]:
        c += 1

print(c)

for i in range(1, m + 1):
    if not nums[i]:
        print(i, end=" ")