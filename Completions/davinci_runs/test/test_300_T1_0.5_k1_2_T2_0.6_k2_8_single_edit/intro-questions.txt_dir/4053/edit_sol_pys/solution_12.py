
import sys
n = int(sys.stdin.readline())
prefixes = []
suffixes = []
for i in range(n-1):
    prefixes.append(sys.stdin.readline().strip())
for i in range(n-1):
    suffixes.append(sys.stdin.readline().strip())

def contains(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

prefixes = sorted(prefixes, key=lambda x: len(x))
suffixes = sorted(suffixes, key=lambda x: len(x))

s = ''
for i in range(len(prefixes)):
    if contains(prefixes[i], suffixes[i]):
        s += 'P'
    else:
        s += 'S'
for i in range(len(suffixes)-1, -1, -1):
    if contains(prefixes[i], suffixes[i]):
        s += 'P'
    else:
        s += 'S'
print(s)
print(prefixes)
print(suffixes)
