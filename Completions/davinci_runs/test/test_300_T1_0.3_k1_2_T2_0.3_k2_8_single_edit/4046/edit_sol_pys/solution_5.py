
n = int(input())
q = list(map(int, input().split()))

p = [0]*n
p[0] = q[0]
for i in range(1, n):
    p[i] = p[i-1] + q[i]

if abs(p[-1]) > n:
    print(-1)
else:
    for i in range(n):
        if p[i] < 1 or p[i] > n:
            print(-1)
            break
    else:
        print(*p)
