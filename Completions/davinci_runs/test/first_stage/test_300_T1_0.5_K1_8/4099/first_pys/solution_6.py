

import sys

input_list = sys.stdin.readlines()

n, k, m = map(int, input_list[0].strip().split())
a = list(map(int, input_list[1].strip().split()))

sum_a = sum(a)

goal = n * m

if sum_a >= goal:
    print(0)
    exit()

diff = goal - sum_a

if diff > k:
    print(-1)
else:
    print(diff)