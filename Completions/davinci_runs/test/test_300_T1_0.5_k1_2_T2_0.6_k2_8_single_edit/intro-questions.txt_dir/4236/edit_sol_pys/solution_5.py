

n, m, t = map(int, input().split())

k = 1

while t > 0:
    if t >= m:
        t -= m
    else:
        t -= (t - n)
    k += 1

print(k)
