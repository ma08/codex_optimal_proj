

n = int(input())
prefixes = []
suffixes = []
for _ in range(2*n-2):
    s = input()
    if len(s) == 1:
        prefixes.append(s)
    else:
        suffixes.append(s)

ans = ""
for i in range(n-1):
    if prefixes[i] == suffixes[-1-i]:
        ans += "S"
    else:
        ans += "P"
print(ans)