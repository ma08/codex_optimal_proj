

N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i == N-1:
        ans += 1
        break
    if H[i+1] > H[i]:
        continue
    else:
        ans += 1
    if H[i+2] > H[i+1]:
        continue
    else:
        ans += 1
        i += 1

print(ans)