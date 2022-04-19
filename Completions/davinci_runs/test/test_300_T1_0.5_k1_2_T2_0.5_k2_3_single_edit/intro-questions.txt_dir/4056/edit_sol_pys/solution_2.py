
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1, N):
    ans = lcm(ans, A[i])

print(ans)
