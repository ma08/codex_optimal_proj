

import sys

# read the input
N = int(sys.stdin.readline())
S = []
for _ in range(N):
    S.append(sys.stdin.readline().strip())

# initialize the counter
c = 0

# count the number of ways
for i in range(N):
    if S[i][0] != 'M' and S[i][0] != 'A' and S[i][0] != 'R' and S[i][0] != 'C' and S[i][0] != 'H':
        continue
    for j in range(N):
        if S[j][0] == S[i][0]:
            continue
        if S[j][0] != 'M' and S[j][0] != 'A' and S[j][0] != 'R' and S[j][0] != 'C' and S[j][0] != 'H':
            continue
        for k in range(N):
            if S[k][0] == S[i][0] or S[k][0] == S[j][0]:
                continue
            if S[k][0] != 'M' and S[k][0] != 'A' and S[k][0] != 'R' and S[k][0] != 'C' and S[k][0] != 'H':
                continue
            c += 1

# print the answer
print(c)