import sys


input = sys.stdin.readline()
N, M = [int(i) for i in input.split()]

switches = [[] for _ in range(M)]
for _ in range(M):
    line = [int(i) for i in sys.stdin.readline().split()]
    k = line[0]
    for i in range(1, k+1):
        switches[line[i]-1].append(_)

light_states = [int(i) for i in sys.stdin.readline().split()]

def f(n, ons, cnt):
    if n == M:
        for i in range(M):
            if light_states[i] != ons[i]:
                return 0
        return 1
    if cnt == N:
        return 0
    return f(n, ons+[0], cnt+1) + f(n, ons+[1], cnt+1)

print(f(0, []))
