def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
t = [int(input()) for i in range(n)]

ans = t[0]

for i in t:
    ans = ans * i // gcd(ans, i)

print(ans)
