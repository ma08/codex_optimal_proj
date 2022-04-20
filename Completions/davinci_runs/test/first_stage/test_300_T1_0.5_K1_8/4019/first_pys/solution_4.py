

def spanning_tree(n, m, D, edges):
    if D == 0:
        return "NO"
    if D > n - 1:
        return "YES"
    if D == n - 1:
        return "YES\n" + "\n".join(["{} {}".format(edge[0], edge[1]) for edge in edges])
    if D == 1:
        return "YES\n" + "\n".join(["{} {}".format(edge[1], edge[0]) for edge in edges])
    if D == 2:
        return "YES\n" + "\n".join(["{} {}".format(edge[0], edge[1]) for edge in edges[1:]])
    return "YES\n" + "\n".join(["{} {}".format(edge[1], edge[0]) for edge in edges[:D-2]]) + "\n" + "\n".join(["{} {}".format(edge[0], edge[1]) for edge in edges[D-2:]])

if __name__ == "__main__":
    n, m, D = [int(x) for x in input().split()]
    edges = [tuple([int(x) for x in input().split()]) for _ in range(m)]
    print(spanning_tree(n, m, D, edges))