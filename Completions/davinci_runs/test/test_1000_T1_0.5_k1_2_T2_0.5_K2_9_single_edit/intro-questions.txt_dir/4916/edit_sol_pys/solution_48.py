
import sys

def main():
    input = sys.stdin.readline()
    n,k = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    start = find_start(board,n,k)
    end = find_end(board,n,k)
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
