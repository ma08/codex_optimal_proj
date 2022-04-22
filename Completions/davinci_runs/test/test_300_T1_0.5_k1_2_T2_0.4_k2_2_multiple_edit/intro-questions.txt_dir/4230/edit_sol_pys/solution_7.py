x = int(input().split()[1])
n = int(input().split()[1])
p = [int(i) for i in input().split()]
p.sort()

if x <= p[0]:
    print(p[0]-x)
elif x >= p[-1]:
    print(x-p[-1])
else:
    for i in range(1, n):
        if x <= p[i]:
            print(min(x-p[i-1], p[i]-x))
            break
