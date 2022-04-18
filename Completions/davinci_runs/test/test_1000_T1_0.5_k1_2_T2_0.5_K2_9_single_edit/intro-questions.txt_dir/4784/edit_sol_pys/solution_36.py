

# number of megabytes available per month x
x = int(input("Enter the number of megabytes available per month: "))

# number of months n
n = int(input("Enter the number of months: "))

# list of megabytes spent each month
p = []  # empty list
for i in range(n):
    p.append(int(input("Enter the megabytes spent each month: ")))

# megabytes remaining after n months
remaining = x
for i in range(n):
    remaining = remaining - p[i]
    if remaining < 0:
        remaining = 0

# megabytes available in n+1 month
print("Megabytes available in n+1 month: ", remaining + x)
