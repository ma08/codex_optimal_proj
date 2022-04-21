
import sys

N = int(input())
words = [input() for i in range(N)]

for i in range(N):
    if i == 0 or words[i][0] == words[i-1][-1]:
        continue
    else:
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
            print('No')
            sys.exit()

print('Yes')
