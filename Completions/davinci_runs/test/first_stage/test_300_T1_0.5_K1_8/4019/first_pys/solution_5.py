

#-----Solution-----

#My solution

def find_spanning_tree(n, m, d, edges):
    # If there are not enough edges to form a tree
    if m < n - 1:
        return 'NO'
    # If the degree of the first vertex is already equal to d
    elif d == 0:
        return 'YES'
    # If the degree of the first vertex is greater than d
    elif d < 0:
        return 'NO'
    # If the degree of the first vertex is less than d
    else:
        # Find the edges that are connected to the first vertex
        first_edges = [edge for edge in edges if edge[0] == 1 or edge[1] == 1]
        # If there are not enough edges to form a tree
        if len(first_edges) < n - 1:
            return 'NO'
        # If there are enough edges to form a tree
        else:
            # Check if there is a tree with the required degree
            for i in range(len(first_edges)):
                # Create a set of edges to form a tree
                tree = set(first_edges[:i] + first_edges[i+1:])
                # If the degree of the first vertex is equal to d
                if d == len(tree):
                    return 'YES'
                # If the degree of the first vertex is less than d
                else:
                    # Check if there is a tree with the required degree
                    for edge in first_edges[i+1:]:
                        # Create a set of edges to form a tree
                        tree = set(first_edges[:i] + [edge] + first_edges[i+2:])
                        # If the degree of the first vertex is equal to d
                        if d == len(tree):
                            return 'YES'
            return 'NO'

n, m, d = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

print(find_spanning_tree(n, m, d, edges))

#Solution from the editorial

def find_spanning_tree(n, m, d, edges):
    if m < n - 1:
        return 'NO'
    if d == 0:
        return 'YES'
    if d < 0:
        return 'NO'
    # If there are enough edges to form a tree
    else:
        # Check if there is a tree with the required degree
        for i in range(len(edges)):
            # Create a set of edges to form a tree
            tree = set(edges[:i] + edges[i+1:])
            # If the degree of the first vertex is equal to d
            if d == len(tree):
                return 'YES'
        return 'NO'

n, m, d = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

print(find_spanning_tree(n, m, d, edges))