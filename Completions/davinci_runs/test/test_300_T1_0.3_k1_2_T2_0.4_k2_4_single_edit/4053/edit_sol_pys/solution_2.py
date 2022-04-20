

n = int(input())
prefixes = []
suffixes = []

for i in range(2*n-2):
    s = input()
    if len(s) == n-1:
        prefixes.append(s)
    else:
        suffixes.append(s)

prefixes.sort()
suffixes.sort()

if prefixes[0][0] == prefixes[1][0]:
    print(prefixes[0] + suffixes[0])
else:
    print(prefixes[1] + suffixes[0])
