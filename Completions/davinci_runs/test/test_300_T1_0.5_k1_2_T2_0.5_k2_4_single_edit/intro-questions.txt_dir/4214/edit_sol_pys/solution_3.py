
import math

N = int(input())

towns = []
for i in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

def calc_dist(lst):
    dist = 0
    prev = lst[0]
    for i in lst[1:]:
        # 前の都市までの距離を足す
        dist += math.sqrt((towns[prev][0] - towns[i][0])**2 + (towns[prev][1] - towns[i][1])**2)
        prev = i
    # 都市0に戻る距離を足す
    dist += math.sqrt((towns[prev][0] - towns[lst[0]][0])**2 + (towns[prev][1] - towns[lst[0]][1])**2)
    return dist

# 全組み合わせの数だけループ
total_dist = 0
# 都市0から経路の開始
for i in range(1, N):
    lst = [0, i]
    for j in range(i+1, N):
        lst.append(j)
    total_dist += calc_dist(lst)

# 全組み合わせの数
permutation = math.factorial(N) - 1

# 平均を求める
print(total_dist / len(permutation))
