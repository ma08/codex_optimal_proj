
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

l = A[0][0]
r = A[0][1]
for _ in range(N):
    i = _ + 1
    l = lcm(l, A[i][0])
    r = lcm(r, A[i][1])

print(l+r)
