

import math

n = int(input(""))

l = list(map(int, input("").split()))

count = 0

for i in range(math.floor(n / 3)):
    if l[i] + l[i + 1] > l[i + 2]:
        count += 1

print(count)
