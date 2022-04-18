

# number of megabytes available per month
x = int(input("Enter number of megabytes available per month "))

# number of months
n = int(input("Enter number of months "))

# list of megabytes spent each month
p = []
for i in range(n):
    p.append(int(input("Enter megabytes spent in month " + str(i+1) + " ")))

# megabytes remaining after n months
remaining = x
for i in range(n):
    remaining = remaining - p[i]
    if remaining < 0:
        remaining = 0

# megabytes available in n+1 month
print("Megabytes available in month " + str(n+1) + " is " + str(remaining + x))
