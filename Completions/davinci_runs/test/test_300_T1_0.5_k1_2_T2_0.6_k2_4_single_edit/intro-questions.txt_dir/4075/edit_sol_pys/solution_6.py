
import sys

N, M = map(int, sys.stdin.readline().split())

K_list = []
S_list = []
P_list = []
for i in range(M):
    K_list.append(int(sys.stdin.readline().split()[0]))
    S_list.append(list(map(int, sys.stdin.readline().split())))

P_list = list(map(int, sys.stdin.readline().split()))

# print(N, M)
# print(K_list)
# print(S_list)
# print(P_list)

def make_light(state):
    # print(state)
    i = 0
    while i < M:
        odd_even = sum([1 for j in range(K_list[i]) if state[S_list[i][j]-1] == 1])
        if odd_even % 2 != P_list[i]:
            return False
        i += 1
    return True

def make_state(state, n, N):
    if n == N-1:
        if make_light(state):
            return 1
        else:
            return 0
    else:
        return make_state(state + [1], n+1, N) + make_state(state + [0], n+1, N)

print(make_state([], 0, N))
