

import fractions

def lcm(a, b):
    return a * b // fractions.gcd(a, b)

N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

ans = T[0]
for i in range(1, N):
    ans = lcm(ans, T[i])

print(ans)