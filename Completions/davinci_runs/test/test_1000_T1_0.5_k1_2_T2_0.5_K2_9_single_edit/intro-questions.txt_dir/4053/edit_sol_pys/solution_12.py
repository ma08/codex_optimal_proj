

n = int(input())
prefixes = []
suffixes = []
for i in range(n-1):
    prefixes.append(input())
for i in range(n-1):
    suffixes.append(input())

prefixes = sorted(prefixes, key=lambda x: len(x))
suffixes = sorted(suffixes, key=lambda x: len(x))

s = ''
for i in range(len(prefixes)):
    if prefixes[i] == suffixes[i]:
        s += 'P'
    else:
        s += 'S'
    print(i)
for i in range(len(suffixes)-1, -1, -1):
    if prefixes[i] == suffixes[i]:
        s += 'P'
    else:
        s += 'S'
print(s)
