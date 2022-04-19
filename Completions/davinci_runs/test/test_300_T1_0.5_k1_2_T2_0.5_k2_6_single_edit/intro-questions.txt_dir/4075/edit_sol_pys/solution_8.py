
from itertools import product
import sys

N, M = map(int, sys.stdin.readline().split())

k_list = [int(sys.stdin.readline().split()[0]) for i in range(M)]
s_list = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

p_list = list(map(int, sys.stdin.readline().split()))

def make_state(state, n):
    if n == N:
        return state
    else:
        return make_state(state + [0], n+1) + make_state(state + [1], n+1)

state_list = make_state([], 0)

ans = 0

print(make_state([], 0))
