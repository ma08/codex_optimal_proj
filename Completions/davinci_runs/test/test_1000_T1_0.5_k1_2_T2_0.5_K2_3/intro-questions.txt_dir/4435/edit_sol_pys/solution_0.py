

# SOLUTION

#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split())) # split the input into an array and convert to int

d = [0] * n # create an array with the length of n with 0 values

for i in range(n - 1, -1, -1):
    if i + a[i] < n: # if the current position + a[i] is less than the length of the array, then the next position is i + a[i] and add 1 to the value
        d[i] = d[i + a[i]] + 1
    if i - a[i] >= 0: # if the current position - a[i] is greater or equal to 0, then the next position is i - a[i] and add 1 to the value
        d[i] = min(d[i], d[i - a[i]] + 1)
    if d[i] == 0: # if the current position is 0, then the next position is -1
        d[i] = -1

print(*d) # print the array with a space between each value
