

# SOLUTION

#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

d = [0] * n

for i in range(n - 1, -1, -1):
    if i + a[i] < n: # if the current position + a[i] is less than the length of the array, 
                     # then the next position is i + a[i]
        d[i] = d[i + a[i]] + 1
    if i - a[i] >= 0: # if the current position - a[i] is greater or equal to 0, 
                      # then the next position is i - a[i]
        d[i] = min(d[i], d[i - a[i]] + 1)
    if d[i] == 0: # if the current position is 0, then the next position is -1
        d[i] = -1

print(*d)
