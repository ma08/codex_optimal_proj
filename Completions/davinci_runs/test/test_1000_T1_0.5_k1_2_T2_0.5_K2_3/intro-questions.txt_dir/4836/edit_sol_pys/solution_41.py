

from sys import stdin


def solution(board):
    height = len(board)
    width = len(board[0])
    answer = 0
    for i in range(height):
        for j in range(width):
            if board[i][j] == 1:
                board[i][j] = 0
                answer += 1
    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
from collections import deque

n, k = map(int, stdin.readline().split())
weights = deque(map(int, stdin.readline().split()))  # 큐로 만들기

eaten = set()
while weights and c >= weights[0]:
    c -= weights.popleft()
    eaten.add(c)
print(len(eaten))
