import sys

N, K = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

num_set = set(num)

if len(num_set) < K:
    print(0)
else:
    num_set = sorted(num_set)
    num_len = len(num_set)
    max_num = 0

    for i in range(K):
        max_num = max(max_num, num_set[i])

    print(max_num)
