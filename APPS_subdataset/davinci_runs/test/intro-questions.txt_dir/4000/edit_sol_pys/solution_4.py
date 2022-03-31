
def get_distance(tree, root, node):
    dist = 0
    while node != root:
        dist += 1
        node = tree[node]
    return dist

def find_lca(tree, root, node1, node2):  # find lowest common ancestor
    dist1 = get_distance(tree, root, node1)
    dist2 = get_distance(tree, root, node2)
    if dist1 < dist2:
        node1, node2 = node2, node1
        dist1, dist2 = dist2, dist1
    while dist1 > dist2:
        node1 = tree[node1]
        dist1 -= 1
    while node1 != node2:
        node1 = tree[node1]
        node2 = tree[node2]
    return node1

def solve(n, tree):
    root = 1
    tree = [0] + tree
    lca = [[0] * n for _ in range(n)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            lca[i][j] = lca[j][i] = find_lca(tree, root, i, j)
    max_edges = 0
    best_nodes = (0, 0, 0)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                edges = get_distance(tree, root, i) + get_distance(tree, root, j) + get_distance(tree, root, k) - get_distance(tree, root, lca[i][j]) - get_distance(tree, root, lca[j][k]) - get_distance(tree, root, lca[i][k])
                if edges > max_edges:
                    max_edges = edges
                    best_nodes = (i, j, k)
    return max_edges, best_nodes

def main():
    n = int(input())
    tree = [0] * n
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[b-1] = a
    max_edges, best_nodes = solve(n, tree)
    print(max_edges)
    print(*best_nodes)

if __name__ == "__main__":
    main()
