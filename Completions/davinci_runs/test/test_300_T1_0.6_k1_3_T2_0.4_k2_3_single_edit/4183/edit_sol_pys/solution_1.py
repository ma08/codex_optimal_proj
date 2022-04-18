
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
t = []
for i in range(n):
    t.append(int(input()))

ans = t[0]

for i in t:
    ans = ans * i // gcd(ans, i)

print(ans)
