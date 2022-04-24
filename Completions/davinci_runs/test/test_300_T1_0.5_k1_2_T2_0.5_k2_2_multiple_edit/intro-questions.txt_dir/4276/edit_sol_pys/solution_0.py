import sys
sys.setrecursionlimit(10**6)

def dfs(curr_node, curr_cost):
    global min_cost
    if curr_node == dst:
        min_cost = min(min_cost, curr_cost)
        return
    elif curr_cost > min_cost:
        return
    else:
        for i in range(n):
            if not visited[i] and cost[curr_node][i] != -1:
                visited[i] = True
                dfs(i, curr_cost + cost[curr_node][i])
                visited[i] = False

def main():
    global n, cost, visited, min_cost, dst
    n = int(sys.stdin.readline())
    cost = [[-1 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for i in range(n):
            cost[line[0] - 1][i] = line[i + 1]
    k = int(sys.stdin.readline())
    for _ in range(k):
        src, dst = map(int, sys.stdin.readline().split())
        src -= 1
        dst -= 1
        visited = [False for _ in range(n)]
        min_cost = 10**8
        visited[src] = True
        dfs(src, 0)
        if min_cost == 10**8:
            print(-1)
        else:
            print(min_cost)

if __name__ == "__main__":
    main()
