import sys

x = int(input())
n = int(input())
p = list(map(int, input().split()))
p.sort()
if x < p[0]:
    sys.stdout.write(str(p[0] - x))
elif x > p[n-1]:
    sys.stdout.write(str(x - p[n-1]))
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                sys.stdout.write(str(p[i-1] - x))
            else:
                sys.stdout.write(str(p[i] - x))
            break
