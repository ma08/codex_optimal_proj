

def adj_list(n, edges):
    adj = [[] for _ in range(n+1)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    return adj[1:]

def eulerian_cycle(adj):
    n = len(adj)
    cycle = []
    stk = [1] # start from node 1
    while stk:
        v = stk[-1]
        if not adj[v-1]: # if no edges coming out of v
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
