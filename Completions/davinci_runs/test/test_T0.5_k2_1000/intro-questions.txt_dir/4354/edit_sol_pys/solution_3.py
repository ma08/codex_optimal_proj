
N,M = map(int,input().split())
students = [list(map(int,input().split())) for i in range(N)]
checkpoints = [list(map(int,input().split())) for i in range(M)]

for i in range(N):
    dist = []
    for j in range(M):
        dist.append(abs(students[i][0]-checkpoints[j][0])+abs(students[i][1]-checkpoints[j][1]))
    print(dist.index(min(dist))+1)
