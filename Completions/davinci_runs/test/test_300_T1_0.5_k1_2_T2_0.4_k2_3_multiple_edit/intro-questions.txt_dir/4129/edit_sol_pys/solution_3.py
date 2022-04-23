

import sys
import os

def main():
    n, m, s = map(int, sys.stdin.readline().strip().split())
    roads = []
    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split()) # 경로 입력
        roads.append((u, v))

    # Graph, Adjacency list
    graph = [[] for i in range(n+1)] # 그래프 초기화
    for (u, v) in roads:
        graph[u].append(v) # 경로 추가

    # DFS
    visited = [False for i in range(n+1)] # 방문 여부 초기화
    stack = [s] # 시작 노드 추가
    while stack:
        u = stack.pop() # 현재 노드
        visited[u] = True # 방문 체크
        for v in graph[u]: # 현재 노드와 연결된 노드들
            if not visited[v]: # 방문하지 않았다면
                stack.append(v) # 스택에 추가

    # Count
    res = 0
    for i in range(1, n+1): # 모든 노드에 대해
        if i == s: # 시작 노드는 무시
            continue
        if not visited[i]: # 방문하지 않았다면
            res += 1 # 카운트 증가

    print(res)


if __name__ == '__main__':
    main()
