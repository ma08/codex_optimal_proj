

x = int(input())
n = int(input())
p = list(map(int, input().split()))
s = 0
p.sort()

if x < p[0]:
    s = p[0] - x
elif x > p[n-1]:
    s = x - p[n-1]
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                s = p[i-1] - x
            else:
                s = p[i] - x
print(s)
            break
