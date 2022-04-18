
from sys import stdin

N = int(stdin.readline())
S = stdin.readline().rstrip()

cnt = 0
max_cnt = 0

for i in range(N):
    if S[i] == 'I':
        cnt += 1
    else:
        cnt -= 1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
