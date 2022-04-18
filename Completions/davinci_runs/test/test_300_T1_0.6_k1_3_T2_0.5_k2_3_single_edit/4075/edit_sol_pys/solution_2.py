
import itertools
N, M = map(int, input().split())

bulbs = []
for i in range(M):
    bulbs.append(list(map(int, input().split())))

p = list(map(int, input().split()))

ans = 0
for on in itertools.product([0,1], repeat=N):
    flag = True
    for j in range(M):
        cnt = 0
        for k in range(bulbs[j][0]):
            if bulbs[j][k+1] in on:
                cnt += 1
        if (cnt % 2) != p[j]:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
