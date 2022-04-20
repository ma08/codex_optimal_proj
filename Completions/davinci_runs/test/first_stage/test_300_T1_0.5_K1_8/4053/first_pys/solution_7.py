

n = int(input())
prefixes = []
suffixes = []
for i in range(2*n-2):
    s = input()
    if len(s) == 1:
        prefixes.append(s)
    else:
        suffixes.append(s)

prefixes.sort()
suffixes.sort()

ans = []
for i in range(n-1):
    if prefixes[i][0] == suffixes[i][0]:
        ans.append("P")
    else:
        ans.append("S")

for i in ans:
    print(i, end="")