
# -----Constants-----
MOD = 10 ** 9 + 7 

# -----Functions-----
def gcd(a,b):
    while a != 0: a, b = b % a, a
    return b 

# -----Input and Output-----
[K] = [int(input()) for i in range(1)] 

# -----Solve-----
ans = 0 
for a in range(1, K + 1):
    for b in range(1, K + 1): 
        for c in range(1, K + 1): 
            ans += gcd(a, gcd(b, c)) 
print(ans % MOD) 
