# 백준에서 문제를 받아와서 풀기
import sys
sys.stdin = open("input.txt")


N,M = map(int,input().split()) # N은 사람의 수, M은 가능한 위치의 수
student = [list(map(int,input().split())) for i in range(N)] # 사람의 위치 정보
checkpoint = [list(map(int,input().split())) for i in range(M)] # 가능한 위치의 정보

for i in range(N):
    dist = [] # 사람마다 최단거리를 담을 리스트
    for j in range(M):
        dist.append(abs(student[i][0]-checkpoint[j][0])+abs(student[i][1]-checkpoint[j][1]))
    print(dist.index(min(dist))+1)
