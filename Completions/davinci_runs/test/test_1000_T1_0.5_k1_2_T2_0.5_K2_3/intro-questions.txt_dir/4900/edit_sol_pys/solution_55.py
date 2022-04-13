

def main():
    # read in the number of villages
    n = int(input())

    # read in the weight of each edge
    weights = []
    for i in range(n):
        weights.append([int(x) for x in input().split()])

    # find the minimum spanning tree of the graph
    # the algorithm we use is Prim's algorithm
    # the algorithm is explained in detail here:
    # https://en.wikipedia.org/wiki/Prim%27s_algorithm
    # a good visualization of the algorithm can be found here:
    # https://www.cs.usfca.edu/~galles/visualization/Prim.html

    # create a list of all the vertices
    vertices = [i for i in range(n)]

    # the set of vertices that have been visited
    visited = set()

    # the set of vertices that have not been visited
    not_visited = set(vertices)

    # the set of edges that are in the minimum spanning tree
    # each edge is represented as a tuple (u, v)
    # where u is the vertex that is already in the visited set
    # and v is the vertex that is being added to the visited set
    edges = []

    # start at vertex 0
    current_vertex = 0

    # while there are still vertices to visit
    while len(not_visited) > 0:
        # add the current vertex to the visited set
        visited.add(current_vertex)
        not_visited.remove(current_vertex)

        # find the vertex that is closest to the current vertex
        # that has not been visited yet, and add it to the MST
        min_weight = float("inf")
        min_edge = None
        for vertex in not_visited:
            if weights[current_vertex][vertex] < min_weight:
                min_weight = weights[current_vertex][vertex]
                min_edge = (current_vertex, vertex)

        # if a vertex has been found, then add it to the visited set
        # and add the edge that connects it to the current vertex
        # to the set of edges
        if min_edge is not None:
            visited.add(min_edge[1])
            not_visited.remove(min_edge[1])
            edges.append(min_edge)

        # move to the next vertex
        current_vertex = min_vertex

    # output the edges
    for edge in edges:
        print(edge[0] + 1, edge[1] + 1)

if __name__ == '__main__':
    main()
