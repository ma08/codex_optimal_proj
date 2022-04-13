

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(board,n,k,start):
    queue = deque()
    queue.append(start)
    visited = [[0]*n for _ in range(n)]
    visited[start[0]][start[1]] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # if board[nx][ny] == k:
                #     return visited[x][y]
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return -1

import sys

def main():
    input = sys.stdin.readline
    n,k = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    # print(board)
    # print(n,k)

    # print(find_start(board,n,k))
    # print(find_end(board,n,k))
    start = find_start(board,n,k)
    end = find_end(board,n,k)
    # print(start,end)
    if start and end:
        print(manhattan_dist(start,end))
    else:
        print(-1)


def find_start(board,n,k):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                return (i,j)
    return None

def find_end(board,n,k):
    for i in range(n):
        for j in range(n):
            if board[i][j] == k:
                return (i,j)
    return None

def manhattan_dist(start,end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

if __name__ == "__main__":
    main()
