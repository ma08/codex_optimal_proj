

def main():
    # read in the number of vertices
    n = int(input()) 

    # read in the distances between each pair of vertices
    distances = []
    for i in range(n):
        distances.append([int(x) for x in input().split()])

    # the set of vertices that have been visited
    visited = set() 

    # the set of vertices that have not been visited
    not_visited = set([i for i in range(n)]) 

    # the set of edges that have been visited
    edges = [] 

    current_vertex = 0 

    while len(not_visited) > 0:
        visited.add(current_vertex) 
        not_visited.remove(current_vertex) 

        min_distance = float("inf") 
        min_vertex = None 
        for vertex in not_visited:
            if distances[current_vertex][vertex] < min_distance:
                min_distance = distances[current_vertex][vertex]
                min_vertex = vertex

        if min_vertex is not None:
            visited.add(min_vertex) 
            not_visited.remove(min_vertex) 
            edges.append((current_vertex, min_vertex))

        current_vertex = min_vertex 

    for edge in edges:
        print(edge[0] + 1, edge[1] + 1) 

if __name__ == '__main__':
    main()
