# https://atcoder.jp/contests/abc074/tasks/arc083_b

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += 1 / A[i]

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
