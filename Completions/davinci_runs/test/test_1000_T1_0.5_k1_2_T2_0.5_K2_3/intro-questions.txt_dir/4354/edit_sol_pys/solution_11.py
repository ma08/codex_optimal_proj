

N,M = map(int,input().split())
student = [list(map(int,input().split())) for i in range(N)]
checkpoint = [list(map(int,input().split())) for i in range(M)]

for i in range(N):
    dist = []#거리를 저장할 리스트
    for j in range(M):
        dist.append(abs(student[i][0]-checkpoint[j][0])+abs(student[i][1]-checkpoint[j][1]))#거리 계산
    print(dist.index(min(dist))+1)#가장 가까운 체크포인트 출력
