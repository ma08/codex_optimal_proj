

def main():
    # read in the number of villages
    n = int(input())

    # read in the distances between each pair of villages
    distances = []
    for i in range(n):
        distances.append([int(x) for x in input().split()])

    # find the minimum spanning tree of the graph
    # the algorithm we use is Kruskal's algorithm
    # the algorithm is explained in detail here: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    # a good visualization of the algorithm can be found here: https://www.cs.usfca.edu/~galles/visualization/Kruskal.html

    # create a list of all the vertices
    vertices = [i for i in range(n)]


if __name__ == '__main__':
    main()
