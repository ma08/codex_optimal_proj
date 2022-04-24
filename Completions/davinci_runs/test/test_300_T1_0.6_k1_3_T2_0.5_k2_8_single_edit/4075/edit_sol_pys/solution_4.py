

import sys
N, M = [int(i) for i in sys.stdin.readline().split()]

switches = [[] for _ in range(N)]
for _ in range(M):
    k = int(sys.stdin.readline())
    line = [int(i) for i in sys.stdin.readline().split()[:k]]
    for i in range(k):
        switches[line[i]-1].append(_)

light_states = [int(i) for i in sys.stdin.readline().split()]

def f(n, ons, ans):
    if n == N:
        if sum([1 for i in range(M) if light_states[i] == 1 and sum([1 for j in switches[i] if ons[j] == 1]) % 2 == 0]) == 0:
            ans += 1
    else:
        f(n+1, ons+[0], ans)
        f(n+1, ons+[1], ans)

ans = 0
f(0, [], ans)
print(ans)
