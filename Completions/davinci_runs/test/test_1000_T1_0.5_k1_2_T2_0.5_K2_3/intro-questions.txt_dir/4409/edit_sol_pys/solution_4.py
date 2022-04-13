
import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    #print(a)
    
    # build list of indices of first and last element of each contiguous sequence of equal elements
    indices = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[j] == a[i]:
            j += 1
        indices.append((i, j - 1))
        i = j
    #print(indices)
    
    # build graph
    # each node is a contiguous sequence of equal elements
    # edges are added between two nodes if the two nodes are adjacent in the array
    # the weight of each edge is the distance between the two nodes
    adj_list = {}
    for i in range(len(indices)):
        adj_list[i] = []
    for i in range(len(indices) - 1):
        (x1, y1) = indices[i]
        (x2, y2) = indices[i + 1]
        if y1 == x2 - 1:
            adj_list[i].append((i + 1, a[y1] - a[x2]))
        elif x1 == y2 + 1:
            adj_list[i + 1].append((i, a[x1] - a[y2]))
    #print(adj_list)
    
    # use dijkstra's algorithm to find the shortest path from any node to the node containing the smallest value
    # the shortest path from any node to the node with the smallest value is the path that results in the smallest value
    # the path from any node to the node containing the smallest value can be found by starting from the node containing the smallest value and going backwards
    min_node = min(adj_list, key=lambda x: a[indices[x][0]])
    dist = {}
    for i in range(len(indices)):
        dist[i] = float('inf')
    dist[min_node] = 0
    q = deque()
    q.append(min_node)
    while q:
        u = q.popleft()
        for v, w in adj_list[u]:  # v = node, w = weight
            if dist[v] > dist[u] + w:  # if the distance to reach v is greater than the distance to reach u + the weight of the edge from u to v
                dist[v] = dist[u] + w  # update the distance to reach v
                q.append(v)  # add v to the queue
    #print(dist)
    
    # generate output
    # the output is the path from any node to the node with the smallest value
    # the path from any node to the node containing the smallest value can be found by starting from the node containing the smallest value and going backwards
    output = []
    curr_node = min_node
    while curr_node != 0:  # while the current node is not the first node
        for v, w in adj_list[curr_node]:  # v = node, w = weight
            if dist[curr_node] == dist[v] + w:  # if the distance to reach curr_node is equal to the distance to reach v + the weight of the edge from v to curr_node
                if w > 0:  # if the weight of the edge from v to curr_node is positive
                    output.append((1, curr_node + 1, v + 1))  # add a move command to the output
                else:  # if the weight of the edge from v to curr_node is negative
                    output.append((2, curr_node + 1, v + 1))  # add a reverse command to the output
                curr_node = v  # update curr_node
                break
    #print(output)
    
    print(len(output))
    for op in output:
        print(' '.join([str(x) for x in op]))
    
if __name__ == '__main__':
    main()
