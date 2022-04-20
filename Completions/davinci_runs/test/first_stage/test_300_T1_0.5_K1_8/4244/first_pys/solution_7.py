

N = int(input())
X = list(map(int, input().split()))

ans = 0
for x in X:
    ans += x**2
ans -= sum(X)**2 / N
print(int(ans))