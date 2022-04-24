

N, A, B = map(int, input().split())

c = gcd(A, B)
lcm = A * B / c
k = N // lcm
ans = A * k + min(N % lcm, A)

print(ans)
