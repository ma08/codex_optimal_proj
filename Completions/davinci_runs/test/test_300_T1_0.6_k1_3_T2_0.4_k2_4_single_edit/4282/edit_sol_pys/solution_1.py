
def adj_list(n, a):
    adj = [[] for _ in range(n)]
    for i in range(n):
        adj[a[i][0] - 1].append(i + 1)
        adj[a[i][1] - 1].append(i + 1)
    return adj

def eulerian_cycle(adj):
    n = len(adj)
    cycle = []
    stk = [1]
    while stk:
        v = stk[-1]
        if not adj[v - 1]:
            cycle.append(v)
            stk.pop()
        else:
            w = adj[v - 1].pop()
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
