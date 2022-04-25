n = int(input())
prefixes = []
suffixes = []
for i in range(n):
    prefixes.append(input())
for i in range(n):
    suffixes.append(input())

prefixes = sorted(prefixes, key=lambda x: len(x), reverse=True)
suffixes = sorted(suffixes, key=lambda x: len(x), reverse=True)

s = ''
for i in range(len(prefixes)):
    if prefixes[i] == suffixes[i]:
        s += 'P'
    else:
        s += 'S'
for i in range(len(suffixes)):
    if prefixes[i] == suffixes[i]:
        s += 'P'
    else:
        s += 'S'
print(s)
