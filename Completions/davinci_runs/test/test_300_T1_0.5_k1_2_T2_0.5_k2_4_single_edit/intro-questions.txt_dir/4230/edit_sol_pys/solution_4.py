

x = int(input())
n = int(input())
p = list(map(int, input().split()))

p.sort()

if x <= p[0]:
    print(abs(p[0] - x))
elif x >= p[n-1]:
    print(abs(x - p[n-1]))
else:
    for i in range(1, n):
        if p[i-1] <= x and x <= p[i]:
            if abs(p[i-1] - x) <= abs(p[i] - x):
                print(abs(p[i-1] - x))
            else:
                print(abs(p[i] - x))
            break
