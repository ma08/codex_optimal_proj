

h, n, m = map(int, input().split())

a = 0
b = 0

for i in range(1, h+1):
    a += (2*i - 1)
    b += (2*i)

if a <= n:
    print(0, 0)
else:
    a -= n
    if a <= m:
        print(a, 0)
    else:
        print(m, 0)
