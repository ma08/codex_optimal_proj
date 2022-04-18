
N = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    ans += abs(h[i] - h[i+1])

print(ans)
