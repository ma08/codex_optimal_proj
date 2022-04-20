import sys

n = int(input())
prefixes = []
suffixes = []
for i in range(n-1):
    prefixes.append(sys.stdin.readline().strip())
for i in range(n-1):
    suffixes.append(sys.stdin.readline().strip())

prefixes = sorted(prefixes, key=lambda x: len(x))
suffixes = sorted(suffixes, key=lambda x: len(x))

s = []
for i in range(len(prefixes)):
    if prefixes[i] == suffixes[i]:
        s.append('P')
    else:
        s.append('S')
for i in range(len(suffixes)-1, -1, -1):
    if prefixes[i] == suffixes[i]:
        s.append('P')
    else:
        s.append('S')
print(''.join(s))
