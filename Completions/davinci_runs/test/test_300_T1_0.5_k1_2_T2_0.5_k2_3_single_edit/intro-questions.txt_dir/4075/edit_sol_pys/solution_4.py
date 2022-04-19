
import sys

N, M = map(int, sys.stdin.readline().split())  # N: 電球の数, M: スイッチの数

k_list = []  # スイッチが何個の電球を操作するか
s_list = []  # スイッチがどの電球を操作するか
for i in range(M):
    k_list.append(int(sys.stdin.readline().split()[0]))
    s_list.append(list(map(int, sys.stdin.readline().split())))

p_list = list(map(int, sys.stdin.readline().split()))  # 電球の状態

def check_light(state):
    """
    入力された電球の状態に応じて、スイッチが操作する電球の状態を調べる
    全ての電球が点灯しているならTrue, それ以外はFalse
    """
    for i in range(M):
        odd_even = 0  # 奇数なら1, 偶数なら0
        for j in range(k_list[i]):
            if state[s_list[i][j]-1] == 1:
                odd_even += 1  # 奇数なら1を足し続ける
        if odd_even % 2 != p_list[i]:
            return False
    return True

def make_state(state, n):  # 電球の状態を全て試す
    """
    入力された電球の状態を全て試す
    全ての電球が点灯している状態の数を返す
    """
    if n == N:
        if check_light(state):
            return 1
        else:
            return 0
    else:
        return make_state(state + [1], n+1) + make_state(state + [0], n+1)

print(make_state([], 0))
