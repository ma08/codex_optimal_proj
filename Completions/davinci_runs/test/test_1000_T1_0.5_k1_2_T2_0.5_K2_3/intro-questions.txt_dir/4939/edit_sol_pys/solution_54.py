import sys
sys.stdin = open('input.txt', 'r')

def check(i, j, k):
    global cnt
    if k == 7:
        cnt += 1
        return
    if i + 1 < N and j + 1 < N:
        if board[i][j] == board[i + 1][j + 1]:
            check(i + 1, j + 1, k + 1)
    if i + 1 < N:
        if board[i][j] == board[i + 1][j]:
            check(i + 1, j, k + 1)
    if j + 1 < N:
        if board[i][j] == board[i][j + 1]:
            check(i, j + 1, k + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            check(i, j, 1)
    print('#{} {}'.format(tc, cnt))
