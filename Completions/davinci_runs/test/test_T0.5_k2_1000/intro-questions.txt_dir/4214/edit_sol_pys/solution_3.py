
import math

N = int(input())

towns = []
for i in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

def calc_dist(lst):
    dist = 0
    for i in range(len(lst)):
        if i == len(lst) - 1:
            dist += math.sqrt((lst[i][0] - lst[0][0])**2 + (lst[i][1] - lst[0][1])**2)
        else:
            dist += math.sqrt((lst[i][0] - lst[i+1][0])**2 + (lst[i][1] - lst[i+1][1])**2)
    return dist

# 全順列を求める(計算量が多いので、実行時間がかかる)
# def calc_permutation(lst):
#     if len(lst) == 1:
#         return [lst]
#     permutation = []
#     for i in range(len(lst)):
#         tmp_lst = lst[:]
#         tmp_lst.pop(i)
#         for e in calc_permutation(tmp_lst):
#             permutation.append([lst[i]] + e)
#     return permutation

# # 全順列の数だけループ
# total_dist = 0
# for p in permutation:
#     # 都市0から経路の開始
#     dist = 0
#     prev = 0
#     for i in p:
#         # 前の都市までの距離を足す
#         dist += math.sqrt((towns[prev][0] - towns[i][0])**2 + (towns[prev][1] - towns[i][1])**2)
#         prev = i
#     # 都市0に戻る距離を足す
#     dist += math.sqrt((towns[prev][0] - towns[0][0])**2 + (towns[prev][1] - towns[0][1])**2)
#     total_dist += dist

# 平均を求める
print(calc_dist(towns) / math.factorial(N))
