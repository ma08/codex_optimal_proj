

import sys

N = int(sys.stdin.readline())
d_list = []
for i in range(N):
    d_list.append(int(sys.stdin.readline()))
d_list = set(d_list)
print(len(d_list))