
# read input
x = float(input())

# initialize variables
a = 0
c = 0
b = 0

# find solutions
for i in range(1, 10):
    for j in range(1, i):
        for k in range(1, j):
            if i/j + j/k == x:
                a = i
                b = j
                c = k
                break

# print solutions
print(a, b)
