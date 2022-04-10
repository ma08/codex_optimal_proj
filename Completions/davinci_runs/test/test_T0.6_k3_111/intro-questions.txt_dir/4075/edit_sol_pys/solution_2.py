N, M = map(int, input().split())

bulbs = [list(map(int, input().split())) for i in range(M)]
states = list(map(int, input().split()))

possible = 0
for i in range(2**N):
    cnt = 0
    for j in range(M):
        on = sum([(i >> (bulbs[j][k] - 1)) % 2 for k in range(1, bulbs[j][0] + 1)]) % 2
        if on == states[j]:
            cnt += 1
    if cnt == M:
        possible += 1
print(possible)
