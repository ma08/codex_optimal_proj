
import sys

def dfs(v, visited, honest, unkind):
    visited[v] = True  # vを訪問済みにする
    for i in range(len(honest[v])):  # vから出る正直者の辺を調べる
        if not visited[honest[v][i]]:  # 訪問済みでなければ再帰的に調べる
            dfs(honest[v][i], visited, honest, unkind)
    for i in range(len(unkind[v])):  # vから出る不親切な人の辺を調べる
        if not visited[unkind[v][i]]:  # 訪問済みでなければ再帰的に調べる
            dfs(unkind[v][i], visited, honest, unkind)

N = int(input())
honest = [[] for i in range(N)]
unkind = [[] for i in range(N)]
for i in range(N):
    A_i = int(input())
    for j in range(A_i):
        x, y = map(int, sys.stdin.readline().split())
        if y == 1:
            honest[i].append(x-1)
        else:
            unkind[i].append(x-1)
visited = [False] * N
ans = 0
for i in range(N):
    if visited[i]:
        continue
    dfs(i, visited, honest, unkind)
    ans += 1
print(ans)
