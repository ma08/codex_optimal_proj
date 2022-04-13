

import sys

N, M = map(int, sys.stdin.readline().split())

k_list = []
s_list = []
for i in range(M):
    k_list.append(int(sys.stdin.readline().split()[0]))
    s_list.append(list(map(int, sys.stdin.readline().split())))

p_list = list(map(int, sys.stdin.readline().split()))

def make_light(state):
    for i in range(M):
        odd_even = 0
        for j in range(k_list[i]):
            if state[s_list[i][j]-1] == 1:
                odd_even += 1
        if odd_even % 2 != p_list[i]:
            return False
    return True

def make_state(state, n, count):
    if n == N:
        if make_light(state):
            count += 1
        return count
    count = make_state(state + [1], n+1, count) + make_state(state + [0], n+1, count)
    return count

print(make_state([], 0, 0))
