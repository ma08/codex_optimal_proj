

# read input
x = float(input())

# initialize variables
a = 0
b = 0

# find solutions
for i in range(1, 11):
    for j in range(i+1, 11):
        if i/j == x:
            a = i
            b = j
            break

# print solutions
print(a, b)
