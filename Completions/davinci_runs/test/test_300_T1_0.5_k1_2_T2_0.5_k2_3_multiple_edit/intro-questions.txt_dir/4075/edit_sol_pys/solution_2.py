import sys

# N, M = map(int, sys.stdin.readline().split())
N, M = 2, 2

# k_list = []
# s_list = []
# for i in range(M):
#     k_list.append(int(sys.stdin.readline().split()[0]))
#     s_list.append(list(map(int, sys.stdin.readline().split())))

# p_list = list(map(int, sys.stdin.readline().split()))

k_list = [1, 1]
s_list = [[1], [2]]
p_list = [1, 0]

# print(N, M)
# print(k_list)
# print(s_list)
# print(p_list)

# def make_light(state):
#     # print(state)
#     for i in range(M):
#         odd_even = 0
#         for j in range(k_list[i]):
#             if state[s_list[i][j]-1] == 1:
#                 odd_even += 1
#         if odd_even % 2 != p_list[i]:
#             return False
#     return True

# def make_state(state, n):
#     if n == N:
#         if make_light(state):
#             return 1
#         else:
#             return 0
#     else:
#         return make_state(state + [1], n+1) + make_state(state + [0], n+1)

# print(make_state([], 0))

def make_state(state, n):
    if n == N:
        print(state)
        return
    else:
        make_state(state + [0], n+1)
        make_state(state + [1], n+1)

make_state([], 0)
