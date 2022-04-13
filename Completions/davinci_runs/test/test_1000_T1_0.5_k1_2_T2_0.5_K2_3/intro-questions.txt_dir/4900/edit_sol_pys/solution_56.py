

def main():
    # read in the number of villages
    n = int(input())

    # read in the distances between each pair of villages
    distances = []
    for i in range(n):
        distances.append([int(x) for x in input().split()])

    # create a list of all the vertices
    vertices = [i for i in range(n)]

    # the set of vertices that have been visited
    visited = set()

    # the set of vertices that have not been visited
    not_visited = set(vertices)

    # the set of edges that have been visited
    # each edge is represented as a tuple (u, v, w)
    # where u and v are the vertices that the edge connects
    # and w is the weight of the edge
    edges = []

    # start at vertex 0
    current_vertex = 0

    # while there are still vertices to visit
    while len(not_visited) > 0:
        # add the current vertex to the visited set
        visited.add(current_vertex)
        not_visited.remove(current_vertex)

        # find the vertex that is closest to the current vertex
        # that has not been visited yet
        min_distance = float("inf")
        min_vertex = None
        for vertex in not_visited:
            if distances[current_vertex][vertex] < min_distance:
                min_distance = distances[current_vertex][vertex]
                min_vertex = vertex

        # if a vertex has been found, then add it to the visited set
        # and add the edge that connects it to the current vertex
        # to the set of edges
        if min_vertex is not None:
            visited.add(min_vertex)
            not_visited.remove(min_vertex)
            edges.append((current_vertex, min_vertex))

        # move to the next vertex
        current_vertex = min_vertex

    # output the edges
    for edge in edges:
        print(edge[0] + 1, edge[1] + 1)

if __name__ == '__main__':
    main()
