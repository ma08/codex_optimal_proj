

def adj_list(n, a):  # n: number of vertices, a: list of edges
    adj = [[] for _ in range(n+1)]
    for u, v in a:
        adj[u].append(v)
        adj[v].append(u)
    return adj[1:]

def eulerian_cycle(adj):
    n = len(adj)
    cycle = []
    stk = [1]
    while stk:
        v = stk[-1]
        if not adj[v-1]:
            cycle.append(v)
            stk.pop()
        else:
            w = adj[v-1].pop()
            stk.append(w)
    return cycle[::-1]

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, input().split())))
    adj = adj_list(n, a)
    cycle = eulerian_cycle(adj)
    print(' '.join([str(i) for i in cycle]))

if __name__ == '__main__':
    main()
