
import sys
N, M = map(int, sys.stdin.readline().split())

k_list = []
s_list = []
for i in range(M):
    k_list.append(int(sys.stdin.readline().split()[0]))
    s_list.append(list(map(int, sys.stdin.readline().split())))
p_list = list(map(int, sys.stdin.readline().split()))
