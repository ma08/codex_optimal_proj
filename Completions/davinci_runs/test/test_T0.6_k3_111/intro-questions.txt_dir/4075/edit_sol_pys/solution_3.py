
# My answer

N, M = map(int, input().split())

switches = []
for i in range(M):
    switches.append(list(map(int, input().split())))

p = list(map(int, input().split()))

res = 0
for i in range(2**N):
    on = [False]*N
    for j in range(N):
        if (i >> j) & 1:
            on[j] = True

    flag = True
    for j in range(M):
        k = switches[j][0]
        count = 0
        for l in range(k):
            if on[switches[j][l+1]]:
                count += 1
        if count%2 != p[j]:
            flag = False
            break
    if flag:
        res += 1

print(res)
