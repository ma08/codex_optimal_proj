

n = int(input())
prefixes = []
suffixes = []

for i in range(2*n-2):
    s = input()
    if len(s) == 1:
        prefixes.append(s)
    else:
        suffixes.append(s)

for i in range(2*n-2):
    if i < n-1 and prefixes[i] in suffixes:
        print("P", end="")
    elif i >= n-1 and suffixes[i] in prefixes:
        print("S", end="")
