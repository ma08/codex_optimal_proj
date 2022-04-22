

import sys

N = int(input())
word = []

for i in range(N):
    word.append(input())

for i in range(N):
    if i == 0:
        pass
    else:
        if word[i] in word[:i] or word[i][0] != word[i-1][-1]:
            print('No')
            sys.exit()

print('Yes')
