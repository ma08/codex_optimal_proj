

import math

def max_turns(k, n, a, b):
    max_turns_1 = math.floor(k/a)
    max_turns_2 = math.floor(k/b)
    if max(max_turns_1, max_turns_2) < n:
        return -1
    return max(max_turns_1, max_turns_2)

q = int(input())
for _ in range(q):
    k, n, a, b = map(int, input().split())
    print(max_turns(k, n, a, b))
