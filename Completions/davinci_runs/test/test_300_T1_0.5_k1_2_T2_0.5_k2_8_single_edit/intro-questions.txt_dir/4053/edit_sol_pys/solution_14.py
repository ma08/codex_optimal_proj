

n = int(input())
prefixes = []
suffixes = []
for i in range(n-1):
    prefixes.append(input()[::-1])
for i in range(n-1):
    suffixes.append(input()[::-1])

prefixes = sorted(prefixes, key=lambda x: len(x))
suffixes = sorted(suffixes, key=lambda x: len(x))

s = ''
    if prefixes[i] in suffixes[i]:
        s += 'P'
    else:
        s += 'S'
for i in range(len(suffixes)-2, -1, -1):
    if prefixes[i] in suffixes[i]:
        s += 'P'
    else:
        s += 'S'
print(s)
