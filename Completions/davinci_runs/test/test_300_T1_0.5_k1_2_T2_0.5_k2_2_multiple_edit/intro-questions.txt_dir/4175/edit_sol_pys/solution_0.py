

import sys, string
# input
N = int(input())
words = [input() for _ in range(N)]

# check
if N == 1:
    print('Yes')
    sys.exit()

# check
if len(set(words)) != len(words):
    print('No')
    sys.exit()

# check
if words[0][0] != words[1][0] or words[0][-1] != words[-1][-1]:
    print('No')
    sys.exit()

for i in range(N):
    if words[i] in words[:i]:
        print('No')
        sys.exit()

print('Yes')
