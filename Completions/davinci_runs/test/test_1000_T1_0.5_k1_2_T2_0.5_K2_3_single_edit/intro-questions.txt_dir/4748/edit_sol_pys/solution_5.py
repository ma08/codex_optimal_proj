
h, n, m = map(int, input().split())

a_sum = 0
b_sum = 0

for i in range(1, h+1):
    a_sum += (2*i - 1)
    b_sum += (2*i)

if a_sum <= n:
    print(0, m)
else:
    a_sum -= n
    if a_sum <= m*2:
        print(a_sum//2, m - (a_sum//2))
    else:
        print(m, 0)
