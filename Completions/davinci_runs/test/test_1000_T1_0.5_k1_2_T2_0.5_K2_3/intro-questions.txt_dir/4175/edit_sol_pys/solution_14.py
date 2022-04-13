
import sys

N = int(input())
words = set()

for i in range(N):
    words.add(input())

for i in range(N):
    if i == 0:
        continue
    else:
        if words[i] in words[:i] or words[i][0] != words[i - 1][-1]:  # noqa
            print('No')
            sys.exit()

print('Yes')
