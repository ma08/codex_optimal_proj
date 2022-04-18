

n = int(input()) # the length of the word
prefixes = []
suffixes = []
for i in range(n-1): # the prefixes
    prefixes.append(input())
for i in range(n-1): # the suffixes
    suffixes.append(input())

prefixes = sorted(prefixes, key=lambda x: len(x)) # sort the prefixes and suffixes by length
suffixes = sorted(suffixes, key=lambda x: len(x))

s = ''
for i in range(len(prefixes)): # for the prefixes
    if prefixes[i] == suffixes[i]:
        s += 'P'
    else:
        s += 'S'
for i in range(len(suffixes)-1, -1, -1): # for the suffixes
    if prefixes[i] == suffixes[i]:
        s += 'P'
    else:
        s += 'S'
print(s)
