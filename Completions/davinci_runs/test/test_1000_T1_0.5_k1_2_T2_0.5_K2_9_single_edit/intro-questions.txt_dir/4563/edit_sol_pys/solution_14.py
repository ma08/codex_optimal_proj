
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A1 = []
A2 = []
for _ in range(N):
    T, A_ = map(int, input().split())
    A1.append(T)
    A2.append(A_)

l = A1[0]
r = A2[0]
for i in range(1, N):
    l = lcm(l, A1[i])
    r = lcm(r, A2[i])

print(l+r)
