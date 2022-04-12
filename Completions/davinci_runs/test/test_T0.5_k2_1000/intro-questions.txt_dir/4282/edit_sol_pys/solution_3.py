
from collections import defaultdict


def solve(n, a_list):
    d = defaultdict(set)
    for i in range(1, n + 1):
        d[a_list[i][0]].add(i)  # i番目の辺の1つ目の端点
        d[a_list[i][1]].add(i)  # i番目の辺の2つ目の端点
    start = 1
    for i in range(1, n + 1):
        if len(d[i]) == 1:  # この点を始点にすると、最短経路になる
            start = i
            break
    res = []
    for i in range(n):
        res.append(start)
        start = a_list[start][0] if a_list[start][0] != res[-1] else a_list[start][1]  # 次の点を決める
    return ' '.join(map(str, res))


n = int(input())
a_list = defaultdict(list)
for i in range(n):
    a_list[i + 1] = list(map(int, input().split()))
print(solve(n, a_list))
