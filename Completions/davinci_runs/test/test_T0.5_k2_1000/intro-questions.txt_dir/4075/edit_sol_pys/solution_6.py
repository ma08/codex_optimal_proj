
import itertools
import sys

N, M = map(int, sys.stdin.readline().split())

k_list = [0] * M
s_list = [[0] * 10 for i in range(M)]
for i in range(M):
    k_list[i] = int(sys.stdin.readline().split()[0])
    s_list[i] = list(map(int, sys.stdin.readline().split()))

p_list = list(map(int, sys.stdin.readline().split()))

state_list = list(itertools.product([0, 1], repeat=N))

def check_lights(state):
    for i in range(M):
        odd_even = 0
        for j in range(k_list[i]):
            if state[s_list[i][j]-1] == 1:
                odd_even += 1
        if odd_even % 2 != p_list[i]:
            return False
    return True

def make_state(state, n):
    if n == N:
        if check_lights(state):
            return 1
        else:
            return 0
    else:
        return make_state(state + [1], n+1) + make_state(state + [0], n+1)

ans = 0
for state in state_list:
    if check_lights(state):
        ans += 1

print(ans)
