
import numpy as np
from scipy.sparse.csgraph import dijkstra

def main():
    N, D = map(int, input().split())
    L, R = [], []
    for i in range(D):
        l, r = map(int, input().split())
        L.append(l - 1)
        R.append(r - 1)
    graph = np.full((N, N), 10 ** 9)
    for i in range(N):
        graph[i][i] = 0
    for i in range(D):
        graph[L[i]][R[i]] = 1
        graph[R[i]][L[i]] = 1
    dists = dijkstra(graph, directed=False)
    all_sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            all_sum += dists[i][j]
    for i in range(D):
        print(all_sum - dists[L[i]][R[i]])

if __name__ == "__main__":
    main()
