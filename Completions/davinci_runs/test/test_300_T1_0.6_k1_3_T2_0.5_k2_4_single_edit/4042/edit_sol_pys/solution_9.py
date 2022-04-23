

# read input file
with open("file.in") as f:
    x = float(f.readline())

# initialize variables
a = 0
b = 0

# find solutions
for i in range(1, 11):
    for j in range(1, 11):
        if i/j == x:
            a = i
            b = j
            break

# write output file
with open("file.out", "w") as f:
    f.write("%d %d" % (a, b))
