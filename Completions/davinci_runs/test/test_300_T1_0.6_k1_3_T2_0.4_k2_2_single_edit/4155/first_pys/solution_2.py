

N = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += abs(h[i] - (i + 1))

print(ans)