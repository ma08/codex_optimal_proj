

import sys, math

N, K = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

light_list = []
for i in range(K):
    light_list.append(list(map(int, sys.stdin.readline().split())))

P = list(map(int, sys.stdin.readline().split()))

def make_light(state):
    # print(state)
    for i in range(K):
        odd_even = 0
        for j in range(light_list[i][0]):
            if state[light_list[i][j+1]-1] == 1:
                odd_even += 1
        if odd_even % 2 != P[i]:
            return False
    return True

def make_state(state, n):
    if n == N:
        if make_light(state):
            return 1
        else:
            return 0
    else:
        return make_state(state + [1], n+1) + make_state(state + [0], n+1)

print(make_state([], 0))

# print(N, M)
# print(light_list)
# print(P)
