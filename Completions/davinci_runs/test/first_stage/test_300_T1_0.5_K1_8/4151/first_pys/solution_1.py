

n = int(input())
a = list(map(int, input().split()))

#a = [1, 2, 1, 2, 3]
#a = [100, 1]
#a = [1, 3, 3, 7]

#n = len(a)

m = max(a)
c = [0] * (m + 1)

for i in a:
    c[i] += 1

f = [0] * (m + 1)

f[0] = 1
f[1] = 1

for i in range(2, m + 1):
    f[i] = f[i - 1] + f[i - 2]
    f[i] %= 998244353

ans = 1

for i in c:
    ans *= f[i]
    ans %= 998244353

print(ans)