
# -----Constants-----
MOD = 10 ** 9 + 7  # Modulo

# -----Functions-----
def gcd(a, b):  # Greatest Common Divisor
    while a != 0:  # Euclidean Algorithm
        a, b = b % a, a  # b % a == a
    return b  # b == gcd(a, b)

# -----Input and Output-----
[K] = [int(input()) for i in range(1)]

# -----Solve-----
ans = 0  # Initialize Answer
for a in range(1, K + 1):  # Loop for a
    for b in range(1, K + 1):  # Loop for b
        for c in range(1, K + 1):  # Loop for c
            ans += gcd(a, gcd(b, c))  # Calculate gcd(a, b, c)
print(ans % MOD)  # Print Answer
