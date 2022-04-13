
N = int(input())
H = list(map(int, input().split()))

ans = 0
curr = 0
for i in range(1, N):
    if H[i - 1] >= H[i]:
        curr += 1
    else:
        ans = max(ans, curr)
        curr = 0
print(max(ans, curr))
