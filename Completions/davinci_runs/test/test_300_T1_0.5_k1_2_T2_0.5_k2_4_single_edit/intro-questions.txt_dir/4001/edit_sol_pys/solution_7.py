




N = int(input())
divisors = list(map(int, input().split()))
t = 1
s = 1
for i in range(N):
    if divisors[i] == 1:
        continue
    if divisors[i] == divisors[i + 1]:
        t *= divisors[i]
        i += 1
    else:
        s *= divisors[i]
print(t, s)
