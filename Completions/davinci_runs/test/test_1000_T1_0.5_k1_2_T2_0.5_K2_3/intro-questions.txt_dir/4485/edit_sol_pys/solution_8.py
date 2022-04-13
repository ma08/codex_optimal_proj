
N, M = map(int, input().split())

islands = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    islands[a].append(b)
    islands[b].append(a)

for i in islands[1]:
    if N in islands[i]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
