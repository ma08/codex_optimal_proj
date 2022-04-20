
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return a * b // gcd(a, b)
 
N, A, B = map(int, input().split()) 
 
c = gcd(A, B)
lcm = A * B / c
k = N // lcm
ans = A * k + min(N % lcm, A)
 
print(ans)
