
import sys

N, M = map(int, sys.stdin.readline().split())

k_list = list()
s_list = list()
for i in range(M):
    k_list.append(int(sys.stdin.readline().split()[0]))  # k_listに各スイッチのボタン数を格納
    s_list.append(list(map(int, sys.stdin.readline().split())))  # s_listに各スイッチのボタンの番号を格納

p_list = list(map(int, sys.stdin.readline().split()))  # p_listに各電球が点灯するスイッチのボタンの数が奇数なら1, 偶数なら0が格納されている

# print(N, M)  # ボタンの数とスイッチの数
# print(k_list)  # 各スイッチのボタンの数
# print(s_list)  # 各スイッチのボタンの番号
# print(p_list)  # 各電球が点灯するスイッチのボタンの数が奇数なら1, 偶数なら0

def make_light(state):
    # print(state)
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
        if make_light(state):
            return 1
        else:
            return 0
    else:
        return make_state(state + [1], n+1) + make_state(state + [0], n+1)

print(make_state([], 0))
