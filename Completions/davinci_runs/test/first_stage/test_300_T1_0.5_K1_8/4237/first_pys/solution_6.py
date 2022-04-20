

import sys

# read values
vals = sys.stdin.readline().rstrip().split()

# convert to integers
a = int(vals[0])
b = int(vals[1])
c = int(vals[2])
d = int(vals[3])

# initialize count
count = 0

# loop through possible values
for i in range(a, b+1):
    if (i % c != 0) and (i % d != 0):
        count += 1

# print count
print(count)