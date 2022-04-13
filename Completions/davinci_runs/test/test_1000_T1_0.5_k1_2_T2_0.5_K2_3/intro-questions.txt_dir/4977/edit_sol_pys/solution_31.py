

import sys
import heapq

def main():
    n, m = map(int, input().strip().split())
    d = [[0] * n for _ in range(n)]  # 构建邻接矩阵
    for i in range(m):  # 读取边
        a, b, c = map(int, input().strip().split())
        d[a][b] = c
        d[b][a] = c

    q = []  # 创建优先队列
    heapq.heappush(q, (0, 0))  # 将起始点的距离设为0，其他点的距离设为无穷大
    dist = [-1] * n  # 记录距离
    dist[0] = 0  # 起始点的距离设为0
    while q:
        c, v = heapq.heappop(q)  # 取出距离最近的点
        for i in range(n):  # 更新距离
            if d[v][i] and (dist[i] == -1 or dist[i] > c + d[v][i]):
                dist[i] = c + d[v][i]
                heapq.heappush(q, (dist[i], i))

    print(dist[n - 1])  # 输出到终点的最短距离


if __name__ == "__main__":
    main()
