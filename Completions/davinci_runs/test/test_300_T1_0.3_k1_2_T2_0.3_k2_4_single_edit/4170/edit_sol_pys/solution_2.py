
N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if H[i - 1] >= H[i]:
        ans += 1
    elif H[i - 1] == H[i] - 1:
        H[i] -= 1
        ans += 1
print(ans)
