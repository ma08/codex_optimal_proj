import sys

N, K, M = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

lowest_score = M
highest_score = K

while lowest_score < highest_score:
    middle_score = (lowest_score + highest_score) // 2

    total = sum(scores) + middle_score

    if total >= N * M:
        highest_score = middle_score
    else:
        lowest_score = middle_score + 1

if lowest_score >= K:
    print(-1)
else:
    print(lowest_score)
