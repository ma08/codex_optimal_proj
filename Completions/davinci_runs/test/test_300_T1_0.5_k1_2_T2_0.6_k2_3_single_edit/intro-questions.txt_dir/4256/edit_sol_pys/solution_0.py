import math

A,B,C = map(int, input().split())

count = 0
while B >= A and B < C:
    B -= A
    count += 1
print(count)
