
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(n//2)
