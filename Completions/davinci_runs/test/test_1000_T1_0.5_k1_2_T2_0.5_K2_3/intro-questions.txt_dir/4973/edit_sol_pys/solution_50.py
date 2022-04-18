
# https://www.acmicpc.net/problem/2178
import queue

def solution(n, board):
    q = queue.Queue()
    q.put((n-1,n-1))

    visited = set()

    distance = 0

    while not q.empty():
        size = q.qsize()

        for _ in range(size):
            r, c = q.get()

            if (r,c) == (0,0):
                return distance

            if board[r][c] == '#':
                continue

            visited.add((r,c))

            if r+1 < n and (r+1,c) not in visited:
                q.put((r+1,c))
            if r-1 >= 0 and (r-1,c) not in visited:
                q.put((r-1,c))
            if c+1 < n and (r,c+1) not in visited:
                q.put((r,c+1))
            if c-1 >= 0 and (r,c-1) not in visited:
                q.put((r,c-1))

        distance += 1

    return -1

if __name__ == '__main__':
    n = int(input())
    board = [input() for _ in range(n)]
    print(solution(n, board))
