

def min_cost(n, m, a, offers):
    """
    >>> min_cost(3, 2, [1, 3, 3], [(2, 3, 5), (2, 1, 1)])
    5
    >>> min_cost(4, 0, [1, 3, 3, 7], [])
    16
    >>> min_cost(5, 4, [1, 2, 3, 4, 5], [(1, 2, 8), (1, 3, 10), (1, 4, 7), (1, 5, 15)])
    18
    """
    offers = sorted(offers, key=lambda x: x[2])
    tree = {i: [i] for i in range(n)}
    res = 0
    for u, v, w in offers:
        for i in range(n):
            if u in tree[i][1:]:
                u_idx = i
            if v in tree[i][1:]:
                v_idx = i
            if u_idx != None and v_idx != None:
                break
        if u_idx != v_idx:
            res += w
            tree[u_idx][1:] += tree[v_idx][1:]
            tree.pop(v_idx)
    for i in range(n):
        if len(tree[i]) == 2:
            res += a[i]
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for _ in range(m):
        offers.append(tuple(map(int, input().split())))
    print(min_cost(n, m, a, offers))
