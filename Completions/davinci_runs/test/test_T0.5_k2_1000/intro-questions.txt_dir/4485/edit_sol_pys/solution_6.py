
N, M = map(int, input().split())
island = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    island[a].append(b)
    island[b].append(a)
for i in island[1]: # 1번 섬에서 시작
    if N in island[i]: # N번 섬에 도달할 수 있는지 확인
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
