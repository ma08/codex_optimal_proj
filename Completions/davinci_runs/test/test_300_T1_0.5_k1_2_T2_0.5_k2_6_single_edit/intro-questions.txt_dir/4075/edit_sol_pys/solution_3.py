
import sys

N, M = map(int, sys.stdin.readline().split())
k_list = [int(sys.stdin.readline().split()[0]) for i in range(M)]
s_list = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
p_list = list(map(int, sys.stdin.readline().split()))

def make_light(state):
    return all([sum([state[s_list[i][j]-1] for j in range(k_list[i])]) % 2 == p_list[i] for i in range(M)])

def make_state(state, n):
    if n == N:
        return 1 if make_light(state) else 0
    else:
        return make_state(state + [1], n+1) + make_state(state + [0], n+1)

print(make_state([], 0))
