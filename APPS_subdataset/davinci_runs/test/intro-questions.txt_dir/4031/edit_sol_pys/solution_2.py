
from collections import defaultdict

def dfs_topsort(graph):
	"""Performs a depth-first search and returns a topological sort of the graph.
	Raises an exception if the graph has a cycle.
	"""
	# A list to keep track of the visit status of nodes
	visited = [False]*len(graph)
	# A list to store the sorted elements
	top_sort = []

    # Function to perform DFS
    def dfs(node):
        # Mark the current node as visited
        visited[node] = True
        # Recur for all the vertices adjacent to this vertex
        for n in graph[node]:
            if not visited[n]:
                dfs(n)
        # Push current vertex to the stack which stores the result
        top_sort.append(node)

    # Call the recursive helper function to store topological sort starting from all vertices one by one
    for node in range(len(graph)):
        if not visited[node]:
            dfs(node)

    return top_sort[::-1]


def main():
    n = int(input())
    words = [input() for _ in range(n)]

    graph = defaultdict(list)
    for i, word in enumerate(words):
        for j, other in enumerate(words):
            if i == j:
                continue
            if word in other:
                graph[i].append(j)

    try:
        top_sort = dfs_topsort(graph)
    except:
        print("NO")
        return

    print("YES")
    for i in top_sort:
        print(words[i])


if __name__ == "__main__":
    main()
