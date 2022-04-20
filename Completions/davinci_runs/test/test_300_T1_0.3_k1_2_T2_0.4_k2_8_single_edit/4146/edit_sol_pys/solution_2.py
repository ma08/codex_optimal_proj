
import math
import sys

n = int(input())  # read input
v = list(map(int, input().split()))  # read input

counts = {}  # count the number of each value
for i in range(n):
    if v[i] in counts:
        counts[v[i]] += 1
    else:
        counts[v[i]] = 1

if len(counts) > 2:  # if there are more than two different values, then the answer is -1
    print(-1)
    sys.exit()

# if there are only two different values, then the answer is the number of elements of the smaller value
if len(counts) == 2:
    print(math.min(counts[list(counts.keys())[0]], counts[list(counts.keys())[1]]))
    sys.exit()

# if there is only one value, then the answer is the number of elements of that value minus two
print(counts[list(counts.keys())[0]] - 2)
