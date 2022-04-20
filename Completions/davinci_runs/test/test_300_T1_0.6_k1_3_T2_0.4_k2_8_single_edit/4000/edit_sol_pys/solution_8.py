

def main():
    n = int(input())
    adj = [ [] for _ in range(n+1) ]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b) 
        adj[b].append(a) 
    
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    def dfs(cur, par, dep):
        parent[cur] = par
        depth[cur] = dep
        for child in adj[cur]:
            if child != par:
                dfs(child, cur, dep+1)
    
    dfs(1, 0, 0)
    
    def lca(a, b):
        if depth[a] > depth[b]:
            a, b = b, a
        while depth[a] < depth[b]:
            b = parent[b]
        while a != b:
            a = parent[a]
            b = parent[b]
        return a
    
    def solve(x, y, z):
        # x -> y -> z
        p1 = lca(x, y)
        p2 = lca(y, z)
        p3 = lca(x, z)
        d1 = depth[x] + depth[y] - 2 * depth[p1]
        d2 = depth[y] + depth[z] - 2 * depth[p2]
        d3 = depth[x] + depth[z] - 2 * depth[p3]
        return max(d1, d2, d3)
    
    ans = 0
    x, y, z = 0, 0, 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                t = solve(i, j, k)
                if t > ans:
                    ans = t
                    x, y, z = i, j, k
    print(ans)
    print(x, y, z)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
