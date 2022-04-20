

#-----main-----
n = int(input())
t = [int(input()) for _ in range(n)]

# 最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

ans = 1
for i in range(n):
    ans = lcm(ans, t[i])
    
print(ans)