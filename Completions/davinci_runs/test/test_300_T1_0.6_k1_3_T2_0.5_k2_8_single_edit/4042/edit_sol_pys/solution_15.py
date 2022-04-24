
# read input
x = float(input())

# find solutions
for i in range(1, 11):
    for j in range(1, 11):
        if i/j == x:
            print(i, j)
            break
