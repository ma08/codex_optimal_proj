
N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        if i == j:
            continue
        if a[i] % a[j] == 0:
            tmp += 1
    if tmp % 2 == 0:
        ans += (tmp + 2) / (2 * tmp + 2)
    else:
        ans += 0.5

print(ans)
