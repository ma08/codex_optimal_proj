
import sys
input = sys.stdin.readline()
N, M = [int(i) for i in input().split()]

switches = [[] for _ in range(N)]
for _ in range(M):
    line = [int(i) for i in input().split()]
    k = line[0]
    for i in range(k):
        switches[line[i+1]-1].append(_)

light_states = [int(i) for i in input().split()]

def f(n, ons):
    if n == N:
        for i in range(M):
            if light_states[i] == 1 and sum([1 for j in switches[i] if ons[j] == 1]) % 2 == 0:
                return 0
        return 1
    return f(n+1, ons+[0]) + f(n+1, ons+[1])

print(f(0, []))
