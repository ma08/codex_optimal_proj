

import sys

N, M = map(int, sys.stdin.readline().split())

k_list = []
s_list = []
for i in range(M):
    k_list.append(int(sys.stdin.readline().split()[0])) #スイッチの数
    s_list.append(list(map(int, sys.stdin.readline().split()))) #スイッチに接続している電球の番号

p_list = list(map(int, sys.stdin.readline().split())) #電球の点灯状態

# print(N, M)
# print(k_list)
# print(s_list)
# print(p_list)

def make_light(state):
    # 電球の点灯状態とスイッチ押下による点灯状態が一致するか確認
    # print(state)
    for i in range(M):
        odd_even = 0 #電球の点灯数
        for j in range(k_list[i]):
            if state[s_list[i][j]-1] == 1:
                odd_even += 1 #スイッチに接続している電球の点灯数
        if odd_even % 2 != p_list[i]: #電球の点灯数が奇数なら、スイッチを押すと消灯になる
            return False
    return True

def make_state(state, n):
    # 電球の点灯状態を全探索
    if n == N:
        # 全ての電球の点灯状態が決まった
        if make_light(state):
            # スイッチ押下による点灯状態が一致している
            return 1
        else:
            return 0
    else:
        # 電球の点灯状態を全探索
        return make_state(state + [1], n+1) + make_state(state + [0], n+1)

print(make_state([], 0))
