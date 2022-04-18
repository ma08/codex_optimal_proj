

from collections import defaultdict

def read_data():
    n, m = map(int, input().split()) # n is number of nodes and m is number of queries
    graph = defaultdict(list)
    for _ in range(n - 1): # n-1 is the number of edges
        u, v = map(int, input().split()) # u and v are the nodes connected by the edge
        graph[u].append(v)
        graph[v].append(u)
    queries = []
    for _ in range(m): # m is number of queries
        k = int(input()) # k is number of nodes in the query
        v = list(map(int, input().split())) # v is the list of nodes in the query
        queries.append(v)
    return graph, queries

def dfs(graph, start, end):
    visited = set() # set of nodes already visited
    stack = [(start, 0)] # stack of (node, distance) pairs
    while stack:
        node, dist = stack.pop() # pop the last added node and its distance
        if node == end:
            return dist # if node is the end node, return the distance
        if node not in visited:
            visited.add(node) # add the node to the visited set
            for child in graph[node]: # for each child of the node
                if child not in visited:
                    stack.append((child, dist + 1)) # add the child to the stack with distance + 1

def check_query(graph, query):
    start = query[0] # start is the first node in the query
    for v in query[1:]:
        if dfs(graph, start, v) == 1: # if the distance between the start node and the next node is 1, then the next node is the child of the start node
            return True # return true
    return False # return false

def main():
    graph, queries = read_data() # read the data
    for query in queries:
        if check_query(graph, query): # if the query is valid, print YES
            print("YES")
        else:
            print("NO") # otherwise, print NO

if __name__ == "__main__":
    main()
