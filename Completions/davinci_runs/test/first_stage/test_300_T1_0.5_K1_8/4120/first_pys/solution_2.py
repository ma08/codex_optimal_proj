

import heapq
import sys

class Node:
    def __init__(self, id):
        self.id = id
        self.adj = []
        self.visited = False

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    nodes = [Node(i) for i in range(n)]
    for i in range(m):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        nodes[a-1].adj.append(nodes[b-1])
        nodes[b-1].adj.append(nodes[a-1])
    #print(nodes[0].adj[0].id)
    dists = dijkstra(nodes)
    #print(dists)
    print(len(dists))
    for d in dists:
        print(d)

def dijkstra(nodes):
    dist = 0
    dist_nodes = []
    heapq.heappush(dist_nodes, (0, nodes[0]))
    while dist_nodes:
        #print(dist_nodes)
        d, n = heapq.heappop(dist_nodes)
        if n.visited:
            continue
        n.visited = True
        dist += d
        for node in n.adj:
            if node.visited:
                continue
            heapq.heappush(dist_nodes, (1, node))
    return dist

if __name__ == "__main__":
    main()