
# number of months
n = int(input())
# number of megabytes available per month
x = int(input())

# list of megabytes spent each month
p = []
for i in range(n):
    p.append(int(input()))

# megabytes remaining after n months
remaining = x
for i in range(n):
    remaining -= p[i]
    if remaining < 0:
        remaining = 0

# megabytes available in n+1 month
print(remaining + x)
