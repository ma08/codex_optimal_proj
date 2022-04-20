

N, K, Q = map(int, input().split())

aliveList = [K for i in range(N)]

for i in range(Q):
    num = int(input())
    for j in range(N):
        if j+1 == num:
            continue
        aliveList[j] -= 1

for i in range(N):
    if aliveList[i] <= 0:
        print('No')
    else:
        print('Yes')