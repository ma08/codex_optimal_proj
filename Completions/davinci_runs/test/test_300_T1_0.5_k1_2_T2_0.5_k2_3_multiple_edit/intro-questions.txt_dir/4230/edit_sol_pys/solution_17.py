
import sys
x = int(input())  # the position of the center of the segment
n = int(input())
p = list(map(int, input().split()))  # the positions of the centers of the segments

p.sort()

if x < p[0]:
    print(str(p[0] - x))
elif x > p[n-1]:
    print(str(x - p[n-1]))
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                print(str(p[i-1] - x))
            else:
                print(str(p[i] - x))
            break
