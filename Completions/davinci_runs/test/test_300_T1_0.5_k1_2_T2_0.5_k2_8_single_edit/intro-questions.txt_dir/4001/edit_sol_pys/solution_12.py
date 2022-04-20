

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, X = map(int, input().split())
x = list(map(int, input().split()))
x = [abs(x_i - X) for x_i in x]

ans = x[0]
for x_i in x[1:]:
    ans = gcd(ans, x_i)

print(ans)
