
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

def f(n, ons, M):
    if n == N:
        for i in range(M):
            if light_states[i] == 1 and sum([1 for j in switches[i] if ons[j] == 1]) % 2 == 0:
                return 0
        return 1
    return f(n+1, ons+[0], M) + f(n+1, ons+[1], M)

print(f(0, []))
