

N, A, B = map(int, input().split())  # N = 8, A = 3, B = 4

c = gcd(A, B)
lcm = A * B / c
k = N // lcm
ans = A * k + min(N % lcm, A)

print(ans)  # 7
