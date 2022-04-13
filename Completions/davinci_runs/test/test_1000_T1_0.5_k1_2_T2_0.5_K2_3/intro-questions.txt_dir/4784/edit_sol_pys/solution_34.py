

# number of megabytes available per month
x = int(raw_input())

# number of months
n = int(raw_input())

# list of megabytes spent each month
p = []
for i in range(n):
    p.append(int(raw_input()))

# megabytes remaining after n months
remaining = x
for i in range(n):
    remaining = remaining - p[i]
    if remaining < 0:
        remaining = 0

# megabytes available in n+1 month
print(remaining + x)
