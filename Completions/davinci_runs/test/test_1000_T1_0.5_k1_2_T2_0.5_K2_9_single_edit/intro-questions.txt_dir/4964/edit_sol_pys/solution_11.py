

import sys

def main():
    n, h, l = map(int, sys.stdin.readline().split())
    horror = list(map(int, sys.stdin.readline().split()))
    horror_set = set(horror)
    horror_index = [0] * (n + 1)
    for i in horror_set:
        horror_index[i] = 1
    for i in range(l):
        a, b = map(int, sys.stdin.readline().split())
        if a in horror_set:
            horror_index[b] = 1
        elif b in horror_set:
            horror_index[a] = 1
    for i in range(n):
        if horror_index[i] == 1:
            continue
        horror_index[i] = float('inf') # 初期化
        for j in range(1, l + 1):
            a, b = map(int, sys.stdin.readline().split()) # 辺の取得
            if a == i: # 辺の始点が現在の場所なら
                horror_index[i] = min(horror_index[i], horror_index[b] + 1) # 次の場所のコストを比較
            elif b == i: # 辺の終点が現在の場所なら
                horror_index[i] = min(horror_index[i], horror_index[a] + 1) # 次の場所のコストを比較
        if horror_index[i] == float('inf'): # 最短経路が存在しないなら
            horror_index[i] = -1 # -1を代入
    max_hi = max(horror_index)
    max_indices = []
    for i in range(n):
        if horror_index[i] == max_hi:
            max_indices.append(i)
    print(min(max_indices))

if __name__ == '__main__':
    main()
