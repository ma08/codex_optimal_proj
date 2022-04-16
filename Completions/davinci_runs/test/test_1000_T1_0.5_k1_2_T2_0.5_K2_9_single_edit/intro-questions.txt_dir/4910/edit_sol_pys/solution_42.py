
import sys
import math

def get_solution(N):
    if N <= 1:
        return 1
    elif N <= 3:
        return 2
    elif N % 2 == 0:
        return get_solution(N // 2) + 1
    else:
        return get_solution(N // 3) + 1

N = int(sys.stdin.readline())
print(get_solution(N))
