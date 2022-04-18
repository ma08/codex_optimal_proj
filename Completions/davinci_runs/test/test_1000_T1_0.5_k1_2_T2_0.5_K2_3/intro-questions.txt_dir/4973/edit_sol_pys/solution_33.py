import sys


def bfs(board, n, start, end):
    queue = []
    queue.append((start, 0))
    visited = set()
    while queue:
        cur, steps = queue.pop(0)
        if cur == end:
            return steps
        if cur in visited:
            continue
        visited.add(cur)
        for next in board[cur]:
            queue.append((next, steps + 1))
    return -1


def main():
    n = int(sys.stdin.readline())
    board = {}
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        board[i] = []
        for j in range(n):
            if line[j] == '1':
                board[i].append(j)
    print(bfs(board, n, 0, n - 1))


if __name__ == '__main__':
    main()
