

n = int(input())
prefixes = []
suffixes = []

for i in range(n-1):
    s = str(input())
    if len(s) == 1:
        prefixes.append(s)
    else:
        suffixes.append(s)

for i in range(n-1):
    if i < n-1:
        print("P", end="")
    else:
        print("S", end="")
