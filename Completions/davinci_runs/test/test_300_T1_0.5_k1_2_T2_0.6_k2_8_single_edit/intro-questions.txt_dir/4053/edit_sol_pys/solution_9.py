
with open('input.txt') as f:
    n = int(f.readline())
    prefixes = []
    suffixes = []
    for i in range(n-1):
        prefixes.append(f.readline().strip())
    for i in range(n-1):
        suffixes.append(f.readline().strip())
    
    prefixes = sorted(prefixes, key=lambda x: len(x))
    suffixes = sorted(suffixes, key=lambda x: len(x))
    
    s = ''
    for i in range(len(prefixes)):
        if prefixes[i] == suffixes[i]:
            s += 'P'
        else:
            s += 'S'
    for i in range(len(suffixes)-1, -1, -1):
        if prefixes[i] == suffixes[i]:
            s += 'P'
        else:
            s += 'S'
    with open('output.txt', 'w') as out:
        out.write(s)
