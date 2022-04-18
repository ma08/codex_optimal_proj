
import math

N = int(input())

towns = []
for i in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

def calc_dist(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += math.sqrt((towns[route[i]][0] - towns[route[i+1]][0])**2 + (towns[route[i]][1] - towns[route[i+1]][1])**2)
    return dist

def calc_avg(route_list):
    total_dist = 0
    for route in route_list:
        total_dist += calc_dist(route)
    return total_dist / len(route_list)

def calc_permutation(n):
    # 全組み合わせを求める関数
    if n == 1:
        return [[0]]
    permutation = []
    for i in range(n):
        for e in calc_permutation(n-1):
            if i == 0:
                permutation.append([0] + e)
            elif i == n - 1:
                permutation.append(e + [0])
            else:
                permutation.append(e[:i] + [0] + e[i:])
    return permutation

# 平均を求める
print(total_dist / len(permutation))
