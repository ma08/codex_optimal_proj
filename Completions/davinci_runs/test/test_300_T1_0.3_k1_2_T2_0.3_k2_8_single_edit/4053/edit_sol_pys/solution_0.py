

n = int(input())
prefixes = []
suffixes = []

for i in range(2*n-2):
    s = input().strip()
    if len(s) == n-1:
        prefixes.append(s.strip())
    elif len(s) == n:
        suffixes.append(s.strip())

for i in range(n-1):
    for j in range(n-1):
        if prefixes[i] == suffixes[j]:
            print("P", end="")
        else:
            print("S", end="")
    print()
