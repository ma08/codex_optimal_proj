
N = int(input())
H = list(map(int, input().split()))

ans = 0
current = 0
for i in range(N-1):
    if H[i+1] <= H[i]:
        current += 1
    else:
        ans = max(ans, current)
        current = 0
print(max(ans, current))
