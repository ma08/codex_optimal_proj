import sys

N = int(input())
words = []

for i in range(N):
    words.append(input())

if words[0] in words[1:] or words[0][0] != words[1][-1]:
    print('No')
    sys.exit()

print('Yes')
