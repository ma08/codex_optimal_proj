
N, M = map(int, input().split())

bulbs = []
for i in range(M):
    bulbs.append(list(map(int, input().split()))[1:])

p = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    on = []
    for j in range(N):
        if (i >> j) & 1:
            on.append(j+1)
    flag = True
    for j in range(M):
        cnt = 0
        for k in range(len(bulbs[j])):
            if bulbs[j][k] in on:
                cnt += 1
        if (cnt % 2) != p[j]:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
