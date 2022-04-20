
# -----Constants-----
MOD = 10 ** 9 + 7

# -----Functions-----
def gcd(*a):
    while len(a) != 1:
        a = (a[1] % a[0], a[0])
    return a[0]

# -----Input and Output-----
[K] = [int(input()) for i in range(1)]

# -----Solve-----
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(a, gcd(b, c))
print(ans % MOD)
