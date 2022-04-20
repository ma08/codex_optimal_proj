

n = int(input())
a = list(map(int, input().split()))

# first, check if all numbers are equal
if len(set(a)) == 1:
    print(0)
    exit()


# if all numbers are not equal,
# then we need to find the minimum difference between them
# and then add or subtract this difference from the numbers
# so that all numbers are equal

# find the minimum difference
d = min(abs(a[i] - a[i+1]) for i in range(n-1))

# check if all numbers are equal after adding or subtracting d from them
flag = True
for i in range(n-1):
    if abs(a[i] - a[i+1]) % d != 0:
        flag = False
        break

if flag:
    print(d)
else:
    print(-1)