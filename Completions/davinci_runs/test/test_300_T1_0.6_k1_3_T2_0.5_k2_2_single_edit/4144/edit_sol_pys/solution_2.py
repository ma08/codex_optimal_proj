
N = int(input())

a = [0]*(N+1)
a[0] = 1
a[1] = 2
for i in range(2, N+1):
    a[i] = (2*a[i-1] - a[0]) % (10**9+7)
print(a[N])
