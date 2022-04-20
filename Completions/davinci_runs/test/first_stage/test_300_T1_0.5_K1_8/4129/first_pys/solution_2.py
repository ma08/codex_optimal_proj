

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split(" ")]

def read_lines(n):
    return [input() for _ in range(n)]

def read_ints_lines(n):
    return [[int(x) for x in input().split(" ")] for _ in range(n)]

def solve(n, roads):
    #print(roads)
    #print(n, roads)
    adj = [[] for _ in range(n+1)]
    for src, dest in roads:
        adj[src].append(dest)
    #print(adj)
    visited = [False for _ in range(n+1)]
    visited[1] = True
    q = [1]
    while q:
        u = q.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    #print(visited)
    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            ans += 1
    return ans

if __name__ == "__main__":
    n, m, s = read_ints()
    roads = read_ints_lines(m)
    print(solve(n, roads))