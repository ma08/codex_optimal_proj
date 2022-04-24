
import sys

# 중요
sys.setrecursionlimit(10 ** 6)

# 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
cards.sort()

# 재귀함수
def dfs(depth, start):
    if depth == 3:
        if sum(result) == M:
            print(result)
        return
    for i in range(start, N):
        result[depth] = cards[i]
        dfs(depth + 1, i + 1)

# 메인
result = [0] * 3
dfs(0, 0)
