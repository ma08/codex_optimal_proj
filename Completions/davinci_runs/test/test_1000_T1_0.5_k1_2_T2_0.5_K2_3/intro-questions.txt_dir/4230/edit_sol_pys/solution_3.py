
x = float(input())
n = int(input())
p = list(map(float, input().split()))

p.sort()

if x < p[0]:
    print(p[0] - x)
elif x > p[n-1]:
    print(x - p[n-1])
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                print(x - p[i-1])
            else:
                print(x - p[i])
            break
